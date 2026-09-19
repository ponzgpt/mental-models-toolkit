---
name: mental-model-selector
description: Select 1-3 mental models for decisions, prioritization, risk checks, and postmortems.
version: 0.1.0
metadata:
  hermes:
    tags: [mental-models, decision-making, pkm]
    category: reasoning
  openclaw:
    always: true
---
# Mental Model Selector

## When To Use

Use this skill when the user asks for help with:

- a decision
- prioritization
- a tradeoff
- repeated failure
- project focus
- productivity friction
- risk review
- postmortem analysis

## Procedure

1. Read `references/mental_models_index.json` (in this skill folder; in a clone it is also at `data/mental_models_index.json`).
2. Select at most three relevant models.
3. Prefer models that change the next action.
4. Ask only the diagnostic questions needed to reduce ambiguity.
5. Produce one concrete output:
   - decision frame
   - next-action plan
   - risk checklist
   - tradeoff table
   - postmortem review
6. State where the model may mislead.

## Response Format

```text
Selected models: <model ids>
Why these: <one sentence>
Diagnostic questions: <2-5 questions>
Frame: <concise reasoning>
Next action: <one concrete action>
Failure check: <what would make this lens misleading>
```

## Conflict Handling

When two models point in different directions, surface the conflict
directly. Example: `parkinsons_law` may favor a tight deadline while
`second_order_thinking` may reveal that rushing creates expensive
downstream errors.

## Pitfalls

- Do not use more than three models by default.
- Do not turn simple requests into theory.
- Do not present mental models as proof.
- Do not copy source prose from public lists.

## Verification

A useful response helps the user decide or act differently within the current session.
