# Mental Models Toolkit

Agent-readable mental models for decision making, productivity, resilience, and local PKM workflows.

This repository is a compact library of cognitive primitives that an agent can load into context when helping a human think through choices, projects, habits, tradeoffs, and failure modes.

The design is intentionally local-first:

- Markdown files are the source of truth.
- JSON is used only for indexes and schemas.
- Each model is small enough to inject into an agent prompt.
- The library is modular: load one model, one folder, or the full index.
- The output should improve decisions, not create intellectual decoration.

Inspired by public mental-model lists such as this Reddit discussion: https://www.reddit.com/r/selfhelp/comments/utu7v0/30_mental_models_that_will_make_you_more/

## Repository Map

```text
00_CORE/
  mental_model_schema.json       Canonical card schema
  mental_models_agent_skill.md   Agent instructions for using the library
  model_selector.md              Lightweight routing rules
01_DECISION_MAKING/              Models for choices, tradeoffs, and strategy
02_PRODUCTIVITY/                 Models for execution and focus
03_RESILIENCE/                   Models for robustness and adaptation
04_COGNITIVE_BIASES/             Bias checks and decision hygiene
05_GROWTH_AND_LEVERAGE/          Models for scale, compounding, and asymmetric upside
data/
  mental_models_index.json       Machine-readable index
```

## How An Agent Should Use This

1. Read `data/mental_models_index.json`.
2. Select 1-3 relevant models for the user's situation.
3. Load only those model files into context.
4. Ask the model's diagnostic questions.
5. Produce a concrete next action, decision frame, or risk check.

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