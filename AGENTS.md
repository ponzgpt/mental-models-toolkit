# mental-models-toolkit
A mental-model skill pack (30 models) for Hermes Agent and OpenClaw: decisions, prioritisation, risk checks, postmortems. Live: https://mental-models-toolkit.technoir.cloud (README rendered).

## Commands
- Check (before every commit and deploy): `python3 scripts/build_cards.py --check`
- Rebuild cards and the skill's index copy after editing the index: `python3 scripts/build_cards.py`
- Deploy the page: `./scripts/deploy.sh`

## Non-negotiables
1. `data/mental_models_index.json` is canonical; `cards/` and `skills/mental-model-selector/references/` are generated, never hand-edited.
2. Summaries are original wording; never copy a source's prose.
3. Model ids are snake_case data keys; skill slugs are hyphen-case.
4. Agent output always ends in a decision frame, next action, risk check, tradeoff table or postmortem, and says where the model may mislead.
5. Stay a compact decision toolkit, not a self-help encyclopedia.
