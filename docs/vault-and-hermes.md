# Using the toolkit in a Markdown vault and with Hermes

## Install

```bash
hermes skills install ponzgpt/mental-models-toolkit/skills/mental-model-selector
```

The skill carries its own copy of the index (`references/mental_models_index.json`), so it works without cloning the repo.

## Vault layout

Copy `cards/` into your vault, or clone the repo next to it:

```text
MyVault/
  00-inbox/
  decisions/                 one note per decision (journal)
  mental-models/             the 30 cards from cards/
```

Cards link to each other with `[[id|Title]]`, so Obsidian's graph and backlinks work out of the box.

## Front matter for a decision note

```yaml
---
type: decision
date: 2026-09-19
models: [sunk_cost_concorde, regret_minimization]
status: open        # open | decided | reviewed
review_on: 2026-10-19
---
```

`models` uses the card ids, so you can later ask the agent which models you reach for most and whether those decisions held up.

## Prompts

Load the full operating instructions for one conversation:

```text
Read 00_CORE/mental_models_agent_skill.md and use it for the rest of this chat.
I'm deciding whether to take a contract that pays well but eats my evenings.
```

Let the skill select models from the index:

```text
/mental-model-selector Read the model index, pick at most three models for this,
ask me only the questions that change the answer, and give me a risk checklist:
should I move my side project from a VPS to a managed platform?
```

Review past decisions:

```text
List every note in decisions/ with status: decided and review_on before today.
For each, read the cards in its `models` field and ask me what actually happened.
```

See [examples.md](examples.md) for complete worked examples.
