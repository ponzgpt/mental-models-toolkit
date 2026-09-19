"""Generate one Markdown card per model and the skill's bundled index from data/mental_models_index.json.

    python3 scripts/build_cards.py           # write cards/ and the skill copy
    python3 scripts/build_cards.py --check   # fail if anything is invalid or out of date (CI)

data/mental_models_index.json is canonical. Each model gets "card": "cards/<id>.md". The skill ships its own copy
(skills/mental-model-selector/references/) because `hermes skills install` copies only the skill folder.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data" / "mental_models_index.json"
CARDS = ROOT / "cards"
SKILL_COPY = ROOT / "skills" / "mental-model-selector" / "references" / "mental_models_index.json"
REQUIRED = ("id", "title", "category", "tags", "summary", "use_when", "questions", "action", "failure", "related")


def validate(models: list[dict]) -> list[str]:
    errors, ids = [], [m.get("id") for m in models]
    for m in models:
        errors += [f"{m.get('id', '?')}: missing {k}" for k in REQUIRED if not m.get(k)]
        errors += [f"{m['id']}: related '{r}' is not a model" for r in m.get("related", []) if r not in ids]
    errors += [f"duplicate id {i}" for i in {i for i in ids if ids.count(i) > 1}]
    return errors


def card(m: dict, titles: dict[str, str]) -> str:
    q = "\n".join(f"- {x}" for x in m["questions"])
    rel = "\n".join(f"- [[{r}|{titles[r]}]]" for r in m["related"])
    return (f"---\nid: {m['id']}\ncategory: {m['category']}\ntags: [{', '.join(m['tags'])}]\n---\n"
            f"# {m['title']}\n\n{m['summary']}\n\n**Use when:** {m['use_when']}\n\n"
            f"## Diagnostic questions\n\n{q}\n\n## Agent instruction\n\n{m['action']}\n\n"
            f"## Failure mode\n\n{m['failure']}\n\n## Related\n\n{rel}\n")


def render(index: dict) -> dict[Path, str]:
    titles = {m["id"]: m["title"] for m in index["models"]}
    for m in index["models"]:
        m["card"] = f"cards/{m['id']}.md"
    text = json.dumps(index, indent=2, ensure_ascii=False) + "\n"
    out = {INDEX: text, SKILL_COPY: text}
    out.update({CARDS / f"{m['id']}.md": card(m, titles) for m in index["models"]})
    return out


def main(check: bool) -> int:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    errors = validate(index["models"])
    files = render(index)
    stale = {p for p in CARDS.glob("*.md")} - set(files)
    if check:
        errors += [f"out of date: {p.relative_to(ROOT)}" for p, t in files.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        errors += [f"orphan card: {p.relative_to(ROOT)}" for p in stale]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    if not check:
        for p in stale:
            p.unlink()
        for p, t in files.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(t, encoding="utf-8")
    print(f"{len(index['models'])} models ok")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
