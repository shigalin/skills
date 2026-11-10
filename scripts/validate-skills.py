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


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fields = {}
    for line in match.group(1).splitlines() if match else []:
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip('"')
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

    fields = frontmatter(text)
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


def check_version_bump(version):
    """Installed plugin users only receive changes when the version string changes."""

    def git(*args):
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)

    tag = git("describe", "--tags", "--abbrev=0", "--match", "v*")
    if tag.returncode != 0:
        print("note: no release tag found; skipping the version-bump check")
        return
    if tag.stdout.strip() == f"v{version}" and git("diff", "--quiet", tag.stdout.strip(), "--", "skills").returncode == 1:
        error(f"skills/ changed since {tag.stdout.strip()} but the plugin version is still {version}; bump it")


def main():
    skills = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    for skill_dir in skills:
        check_skill(skill_dir)
    version = check_manifests()
    if version:
        check_version_bump(version)

    if errors:
        print(f"{len(errors)} problem(s) found:")
        for message in errors:
            print(f"  - {message}")
        return 1
    print(f"OK: {len(skills)} skills, version {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
