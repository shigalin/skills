#!/usr/bin/env python3
"""Structural checks for the skills and plugin manifests in this repository.

Usage: python3 scripts/validate-skills.py

Exits non-zero and lists every problem found. Uses only the standard library.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = (".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
errors = []


def error(message):
    errors.append(message)


SCALAR = re.compile(
    r'"(?:[^"\\]|\\["\\])*"'  # double-quoted, with only \" and \\ as escapes
    r"|'(?:[^']|'')*'"  # single-quoted, with '' as the escaped quote
    r"|[A-Za-z0-9][A-Za-z0-9 ._/-]*"  # plain scalar free of YAML indicators
)


def frontmatter(name, text):
    """Parse SKILL.md frontmatter, accepting only single-line `key: scalar` entries.

    The standard library has no YAML parser, so any line outside this subset is
    reported as an error instead of being guessed at.
    """
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        error(f"{name}: SKILL.md must start with a frontmatter block closed by '---'")
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        entry = re.fullmatch(r"([A-Za-z][\w-]*): (.+?)\s*", line)
        if not entry or not SCALAR.fullmatch(entry.group(2)):
            error(f"{name}: malformed or unsupported frontmatter line: {line[:60]!r}")
            continue
        key, value = entry.groups()
        if key in fields:
            error(f"{name}: duplicate frontmatter key {key!r}")
        if value[0] == '"':
            value = re.sub(r'\\(["\\])', r"\1", value[1:-1])
        elif value[0] == "'":
            value = value[1:-1].replace("''", "'")
        fields[key] = value
    return fields


def rationale_rows(skill_dir):
    """Yield (failure mode, mapping cell) for each row of the rule-rationale table."""
    path = skill_dir / "references" / "rule-rationale.md"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| **"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            yield re.match(r"\*\*(.+?)\*\*", cells[0]).group(1), cells[-1]


def check_skill(skill_dir):
    name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        error(f"{name}: SKILL.md is missing")
        return
    text = skill_file.read_text(encoding="utf-8")

    fields = frontmatter(name, text)
    if fields.get("name") != name:
        error(f"{name}: frontmatter name {fields.get('name')!r} does not match the directory")
    description = fields.get("description", "")
    if not description or len(description) > 1024:
        error(f"{name}: description must be 1-1024 characters, found {len(description)}")

    # Reference files: every mention resolves, and every file is mentioned.
    mentioned = set(re.findall(r"`references/([\w.-]+\.md)`", text))
    present = {p.name for p in (skill_dir / "references").glob("*.md")}
    for missing in sorted(mentioned - present):
        error(f"{name}: SKILL.md mentions references/{missing}, which does not exist")
    for orphan in sorted(present - mentioned):
        error(f"{name}: references/{orphan} is not listed in SKILL.md")

    # Section headings: numbered ones run 1..n; all titles are available for mapping checks.
    numbered = {int(n): title for n, title in re.findall(r"^## (\d+)\. (.+)$", text, re.M)}
    if sorted(numbered) != list(range(1, len(numbered) + 1)):
        error(f"{name}: numbered sections are not consecutive: {sorted(numbered)}")
    headings = set(numbered.values()) | set(re.findall(r"^## ([^\d\n].*)$", text, re.M))

    # rule-rationale mappings: "N", "N Title", or a multi-word "Title" must match a real heading.
    for mode, cell in rationale_rows(skill_dir):
        for entry in re.split(r";\s*(?![^()]*\))", cell):
            base = re.sub(r"\s*\(.*\)$", "", entry.strip())
            match = re.match(r"^(\d+)(?: (.+))?$", base)
            if match:
                number, title = int(match.group(1)), match.group(2)
                if number not in numbered or (title and numbered[number] != title):
                    error(f"{name}: rule-rationale row '{mode}' maps to '{base}', which is not a section")
            elif re.match(r"^[A-Z][a-z]+( [A-Z][a-z]+)+$", base) and base not in headings:
                error(f"{name}: rule-rationale row '{mode}' maps to '{base}', which is not a heading")

    # Eval scenarios are named after a failure mode that still exists.
    evals = ROOT / "evals" / f"{name}.md"
    if evals.exists():
        modes = {mode for mode, _ in rationale_rows(skill_dir)}
        for scenario, target in re.findall(r"^### (\S+) — (.+)$", evals.read_text(encoding="utf-8"), re.M):
            if target not in modes:
                error(f"evals/{name}.md: scenario {scenario} targets '{target}', which is not in rule-rationale.md")


def check_manifests():
    loaded = {}
    for rel in MANIFESTS + (".claude-plugin/marketplace.json",):
        try:
            loaded[rel] = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            error(f"{rel}: cannot be read as JSON ({exc})")
    if len(loaded) < 3:
        return None

    claude, codex = (loaded[rel] for rel in MANIFESTS)
    for key in ("name", "version"):
        if claude.get(key) != codex.get(key):
            error(f"plugin manifests disagree on {key}: {claude.get(key)!r} vs {codex.get(key)!r}")
    version = str(claude.get("version", ""))
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        error(f"plugin version {version!r} is not MAJOR.MINOR.PATCH")
    listed = [plugin.get("name") for plugin in loaded[".claude-plugin/marketplace.json"].get("plugins", [])]
    if claude.get("name") not in listed:
        error(f"marketplace.json does not list the plugin {claude.get('name')!r}")
    return version


def check_released_version(version):
    """Compare skills/ with the tag of the current version and describe the result.

    Installed plugin users stay on a version until its string changes, so once
    v<version> is tagged, skills/ must not differ from that tag.
    """
    tag = f"v{version}"

    def git(*args):
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).returncode

    try:
        if git("rev-parse", "--git-dir") != 0:
            return "not a git checkout, release-tag check skipped"
        if git("rev-parse", "--quiet", "--verify", f"refs/tags/{tag}") != 0:
            return f"no {tag} tag yet"
        differs = git("diff", "--quiet", tag, "--", "skills")
    except OSError:
        return "git unavailable, release-tag check skipped"
    if differs == 1:
        error(f"skills/ differs from the released tag {tag}; bump the plugin version")
    elif differs != 0:
        error(f"could not compare skills/ with the tag {tag}")
    return f"skills/ matches tag {tag}"


def main():
    skills = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    for skill_dir in skills:
        check_skill(skill_dir)
    version = check_manifests()
    release = check_released_version(version) if version else ""

    if errors:
        print(f"{len(errors)} problem(s) found:")
        for message in errors:
            print(f"  - {message}")
        return 1
    print(f"OK: {len(skills)} skills, version {version} ({release})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
