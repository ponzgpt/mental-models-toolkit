# mental-models-toolkit

Thirty mental models as an agent skill pack: decisions, prioritisation, risk checks, getting unstuck and postmortems. An agent loads the few that fit the problem and asks only the questions those models need. Built for Hermes Agent and OpenClaw; Claude Code and Codex can read it too.

Inspired by public mental-model lists such as this Reddit discussion: https://www.reddit.com/r/selfhelp/comments/utu7v0/30_mental_models_that_will_make_you_more/

The descriptions are original summaries, not copied text.

## Install

```bash
hermes skills install ponzgpt/mental-models-toolkit/skills/mental-model-selector
```

Then see [docs/vault-and-hermes.md](docs/vault-and-hermes.md) for vault layout and prompts, and [docs/examples.md](docs/examples.md) for worked decisions. Every model also exists as an Obsidian-ready card in [`cards/`](cards/).

## Compatibility

- Hermes Agent by Nous Research: `.hermes.md`, `AGENTS.md`, and `skills/mental-model-selector/SKILL.md`.
- OpenClaw by Peter Steinberger: workspace/project skill under `skills/<slug>/SKILL.md`.
- Claude Code and Codex: `AGENTS.md` and plain JSON/Markdown.

## Layout

```text
AGENTS.md                              Shared agent instructions
.hermes.md                             Hermes-native project context
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

## Set up in Hermes Agent

Hermes can scan external skill directories. From a local clone:

```yaml
skills:
  external_dirs:
    - /absolute/path/mental-models-toolkit/skills
```

Then invoke `/mental-model-selector` or let Hermes select the skill naturally.

## Set up in OpenClaw

OpenClaw loads workspace skills from `<workspace>/skills`. Copy or symlink the skill:

```bash
mkdir -p ~/.openclaw/workspace/skills
ln -s /absolute/path/mental-models-toolkit/skills/mental-model-selector ~/.openclaw/workspace/skills/mental-model-selector
openclaw skills list
```

Start a new session or restart the gateway if the skills watcher has not refreshed.

## How an agent should use it

1. Load `skills/mental-model-selector/SKILL.md`.
2. Read `data/mental_models_index.json`.
3. Select at most three relevant models.
4. Ask only the diagnostic questions needed.
5. Produce a concrete decision frame, next action, risk checklist, tradeoff table, or postmortem review.

Do not turn every problem into a model-matching exercise. Use the smallest useful frame.

## Example

User: "I keep switching projects and none of them compound."

Agent:

1. Selects `five_twenty_five_rule`, `compounding_snowball`, and `commitment_bias`.
2. Asks what the user's top goals are and what they keep restarting.
3. Separates exploration from commitment.
4. Produces a 7-day focus constraint and an explicit kill rule.

## Using it yourself

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
review_date: YYYY-MM-DD
---
```

## Verification

```bash
python3 -m json.tool 00_CORE/mental_model_schema.json >/tmp/schema.valid
python3 -m json.tool data/mental_models_index.json >/tmp/index.valid
```

## How this was made

I'm a vibe coder. I decide what to build, write the spec and the rules it has to follow, and test the result until it
does what I said. AI coding agents write the code; I don't write code by hand. Commits under my name were made by an
agent working for me.

## License

MIT.
