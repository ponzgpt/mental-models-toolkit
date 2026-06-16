# mental-models-toolkit

Native mental-model skill pack for agents that help with decisions, prioritization, risk checks, productivity friction, and postmortems.

This repository is a compact library of cognitive primitives that an agent can load into context when helping a human reason through choices and tradeoffs. It is optimized for Hermes Agent and OpenClaw, while remaining readable by Claude Code and Codex.

Inspired by public mental-model lists such as this Reddit discussion: https://www.reddit.com/r/selfhelp/comments/utu7v0/30_mental_models_that_will_make_you_more/

The descriptions here are original operating summaries, not copied source text.

## Compatibility Targets

- Hermes Agent by Nous Research: `.hermes.md`, `AGENTS.md`, and `skills/mental-model-selector/SKILL.md`.
- OpenClaw by Peter Steinberger: workspace/project skill under `skills/<slug>/SKILL.md`.
- Claude Code and Codex: `CLAUDE.md`, `AGENTS.md`, and plain JSON/Markdown.

## Native Entry Points

```text
AGENTS.md                              Shared agent instructions
.hermes.md                             Hermes-native project context
CLAUDE.md                              Claude Code compatibility context
skills.sh.json                         Skill grouping metadata
skills/
  mental-model-selector/SKILL.md       Main installable skill
00_CORE/
  mental_model_schema.json             Canonical model schema
  mental_models_agent_skill.md         Legacy/core agent instructions
  model_selector.md                    Routing notes
data/
  mental_models_index.json             30 machine-readable mental models
```

## Setup For Hermes Agent

Hermes can scan external skill directories. From a local clone:

```yaml
skills:
  external_dirs:
    - /absolute/path/mental-models-toolkit/skills
```

Then invoke `/mental-model-selector` or let Hermes select the skill naturally.

## Setup For OpenClaw

OpenClaw loads workspace skills from `<workspace>/skills`. Copy or symlink the skill:

```bash
mkdir -p ~/.openclaw/workspace/skills
ln -s /absolute/path/mental-models-toolkit/skills/mental-model-selector ~/.openclaw/workspace/skills/mental-model-selector
openclaw skills list
```

Start a new session or restart the gateway if the skills watcher has not refreshed.

## How An Agent Should Use This

1. Load `skills/mental-model-selector/SKILL.md`.
2. Read `data/mental_models_index.json`.
3. Select at most three relevant models.
4. Ask only the diagnostic questions needed.
5. Produce a concrete decision frame, next action, risk checklist, tradeoff table, or postmortem review.

Do not turn every problem into a model-matching exercise. Use the smallest useful frame.

## Example Agent Flow

User: "I keep switching projects and none of them compound."

Agent:

1. Selects `five_twenty_five_rule`, `compounding_snowball`, and `commitment_bias`.
2. Asks what the user's top goals are and what they keep restarting.
3. Separates exploration from commitment.
4. Produces a 7-day focus constraint and an explicit kill rule.

## Human Workflow

Use this repo for:

- Hermes/OpenClaw workspace skills
- Obsidian vaults
- Codex work sessions
- decision journals
- weekly reviews
- project triage

Recommended note front matter:

```markdown
---
models: [second_order_thinking, inversion]
decision_status: draft
review_date: 2026-06-30
---
```

## Verification

```bash
python3 -m json.tool 00_CORE/mental_model_schema.json >/tmp/schema.valid
python3 -m json.tool data/mental_models_index.json >/tmp/index.valid
```

## License

MIT.
