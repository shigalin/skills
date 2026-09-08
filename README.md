<p align="center">
  <img src="./icon.svg" alt="shigalin skills logo" width="160">
</p>

<h1 align="center">shigalin-skills</h1>

<p align="center">
  <a href="https://skills.sh/shigalin/skills"><img src="https://skills.sh/b/shigalin/skills" alt="skills.sh"></a>
</p>

> 💡 Originally rooted in lencx’s hands-on experience — turning hard-won lessons into repeatable execution.

[GitHub](https://github.com/shigalin/skills)


## Installation

Choose either the skills installer or the native plugin. Using both makes each skill available twice.

### Quick Install (Recommended)

```bash
npx skills@latest add shigalin/skills
```

### Specific Install (Global)

```bash
# Claude Code
npx skills@latest add shigalin/skills -a claude-code -g

# Codex
npx skills@latest add shigalin/skills -a codex -g
```

### Plugin Install

#### Codex

```bash
codex plugin marketplace add shigalin/skills
codex plugin add shigalin-skills@shigalin
```

#### Claude Code

```bash
claude plugin marketplace add shigalin/skills
claude plugin install shigalin-skills@shigalin
```

## Skills

- [keel](./skills/keel): Load-bearing architecture design, review, and governance for new and existing systems—authority, ownership, contracts, dependency and state boundaries, recovery, structural change, drift, guards, migration, and deletion.
- [coding-protocol](./skills/coding-protocol): Risk-scaled repository execution and code-evidence guardrails for authority, target scope, evidence, user-work preservation, environment assumptions, verification, and truthful reporting (ref: [Andrej Karpathy's public observations](https://x.com/karpathy/status/2015883857489522876)).

### Recommended Companions

`coding-protocol` and `keel` pair well with:

- [Matt Pocock's Skills](https://github.com/mattpocock/skills) for software engineering workflows.
- [Impeccable](https://github.com/pbakaus/impeccable) for design and UI/UX workflows.

Using them together broadens coverage across product design, engineering practice, architecture governance, and risk-scaled execution. These are independent projects and should be installed separately.

Tip: describe the goal, success criteria, and relevant constraints, then let the agent plan the steps. For example: "Implement this change and make sure the relevant tests pass."

## Model guidance

These skills apply shared task-level principles from provider prompting guides: complete authorized work, keep the requested scope, verify proportionately, and communicate results clearly. The test-commit conditions in coding-protocol are this repository's choice, informed by Anthropic's example, rather than a requirement shared by both guides.

General guidance for independent tool calls, pending results, and user corrections remains in the skills where applicable. Provider-specific parameters and runtime mechanisms, including effort settings, progress rendering, async execution, conversation history, and compaction, belong to the host. The skills neither configure those mechanisms nor assume that delegation or async tools are available.

Reference guides: [OpenAI latest model](https://developers.openai.com/api/docs/guides/latest-model), [Anthropic prompting guides](https://platform.claude.com/docs/zh-CN/build-with-claude/prompt-engineering/prompting-claude-fable-5-1). These adaptations are repository choices, not a measured performance claim; validate behavior on representative tasks in the intended client.

## License

MIT
