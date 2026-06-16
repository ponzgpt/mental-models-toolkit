# Mental Models Toolkit

Agent-readable mental models for decision making, productivity, resilience, and local PKM workflows.

This repository is a compact library of cognitive primitives that an agent can load into context when helping a human think through choices, projects, habits, tradeoffs, and failure modes.

The design is intentionally local-first:

- Markdown files are the source of truth for human and agent instructions.
- JSON is used for the canonical machine-readable model index.
- Each model is small enough to inject into an agent prompt.
- The library is modular: load one category, one model, or the full index.
- The output should improve decisions, not create intellectual decoration.

Inspired by public mental-model lists such as this Reddit discussion: https://www.reddit.com/r/selfhelp/comments/utu7v0/30_mental_models_that_will_make_you_more/

## Repository Map

```text
00_CORE/
  mental_model_schema.json       Canonical card schema
  mental_models_agent_skill.md   Agent instructions for using the library
  model_selector.md              Lightweight routing rules
01_DECISION_MAKING/README.md     Choices, tradeoffs, and strategy
02_PRODUCTIVITY/README.md        Execution and focus
03_RESILIENCE/README.md          Robustness and adaptation
04_COGNITIVE_BIASES/README.md    Bias checks and decision hygiene
05_GROWTH_AND_LEVERAGE/README.md Scale, compounding, and asymmetric upside
data/
  mental_models_index.json       30 machine-readable mental models
```

## How An Agent Should Use This

1. Read `data/mental_models_index.json`.
2. Select 1-3 relevant models for the user's situation.
3. Ask the model's diagnostic questions.
4. Produce a concrete next action, decision frame, or risk check.

Do not turn every problem into a model-matching exercise. Use the smallest useful frame.

## Example Agent Flow

User: "I keep switching projects and none of them compound."

Agent:

1. Selects `five_twenty_five_rule`, `compounding_snowball`, and `commitment_bias`.
2. Asks what the user's top goals are and what they keep restarting.
3. Separates exploration from commitment.
4. Produces a 7-day focus constraint and an explicit kill rule.

## Human Workflow

Use this repo as a prompt pack for:

- Obsidian vaults
- Hermes/Moltbot-style local agents
- Codex work sessions
- decision journals
- weekly reviews
- project triage

Recommended convention for notes:

```markdown
---
models: [second_order_thinking, inversion]
decision_status: draft
review_date: 2026-06-30
---
```

## License

MIT. The model descriptions in this repository are original summaries and operating instructions, not copied source text.
