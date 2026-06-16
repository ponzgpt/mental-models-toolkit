# Agent Context: mental-models-toolkit

This repository publishes mental-model primitives as agent-readable decision skills.

## Primary Runtime Targets

- Hermes Agent: project context through `AGENTS.md` or `.hermes.md`, reusable workflow through `skills/mental-model-selector/SKILL.md`.
- OpenClaw: workspace/project skill under `skills/<slug>/SKILL.md` with short description and hyphen-case name.
- Claude Code and Codex: this file and `CLAUDE.md` provide equivalent project instructions.

## Repository Contract

- Keep skill names lowercase hyphen-case.
- Keep model IDs lowercase snake_case because they are data keys.
- Keep user-facing skill slugs lowercase hyphen-case.
- Do not copy copyrighted model-list prose. Use original summaries and cite inspiration.
- Use JSON for the canonical index and Markdown for agent instructions.
- Agent output must end in a concrete decision frame, next action, or risk check.

## Verification

```bash
python3 -m json.tool 00_CORE/mental_model_schema.json >/tmp/schema.valid
python3 -m json.tool data/mental_models_index.json >/tmp/index.valid
```
