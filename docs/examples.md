# Decision-journal examples

Each entry shows what the user said, which 1–3 models the agent picked and why, and the single output it produced. Use them as the shape to copy, not as advice.

## 1. Choosing which project to focus on

> "I have four side projects and I'm moving none of them forward."

**Models:** `five_twenty_five_rule`, `pareto_principle`, `input_goals`

**Why:** the problem is split attention, not a lack of ideas; the user needs a cut, then a controllable next step.

**Output: decision frame**

| Project | Evidence it matters (not excitement) | Keep? |
|---|---|---|
| A | Two paying users asked for it | Keep |
| B | Nobody has seen it | Park |
| C | Portfolio piece for an active job application | Keep until the application closes |
| D | Fun, no outside signal | Park |

Next action: 45 minutes a day on A, five days a week, for two weeks (an input goal), then review. B and D go in `someday.md`; C gets a fixed end date.

**Where the models mislead:** Pareto assumes the valuable 20% is visible now; a parked project can be the one that would have mattered.

## 2. Quitting a sunk-cost project

> "I've spent eight months on this app. Usage is flat. Stopping feels like wasting all that."

**Models:** `sunk_cost_concorde`, `regret_minimization`, `commitment_bias`

**Why:** the language ("wasting all that") looks backwards; the decision has to be judged on the next months only.

**Output: risk check**

1. Ignoring the eight months, would you start this today with what you now know? (no)
2. What is the cheapest test that could change that answer? (one week, one channel, a numeric bar: 20 new weekly users)
3. If it misses the bar, archive it with a written postmortem so the learning isn't lost.

**Where the models mislead:** some work pays off late (see `compounding_snowball`); the test bar keeps that possibility honest instead of letting it justify drift.

## 3. Tool-comparison paralysis

> "I've been comparing five note-taking apps for two weeks."

**Models:** `paradox_of_choice`, `lindy_effect`, `minimum_viable_product`

**Why:** more comparison won't reduce uncertainty; only using one will.

**Output: next-action plan.** Drop every option younger than two years (Lindy), pick the one with plain-Markdown export (reversible), and use it for one real project for ten days before reconsidering. The criterion for switching: a named task it could not do.

**Where the models mislead:** Lindy undervalues genuinely better new tools; the ten-day trial is the correction.

## 4. Turning an outcome goal into input goals

> "I want 1,000 newsletter subscribers by March."

**Models:** `input_goals`, `goodharts_law`

**Why:** subscribers are an outcome; the user controls writing and distribution.

**Output: tradeoff table**

| Input goal (controllable) | Weekly target | Guards against |
|---|---|---|
| Publish an issue | 1 | Chasing the count with low-effort posts |
| Share in one relevant community, with value in the post | 2 | Spam that grows the list but kills opens |
| Ask 3 readers what they'd forward | 3 conversations | Optimising for sign-ups over usefulness |

Track the outcome monthly, the inputs weekly.

**Where the models mislead:** input goals can become busywork; if inputs are hit for six weeks with no movement, change the inputs.
