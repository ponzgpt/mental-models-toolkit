---
id: redundancy
category: 03_RESILIENCE
tags: [backup, resilience, risk]
---
# Redundancy

Keep spare capacity or backup paths where failure would be expensive.

**Use when:** A single point of failure can break a workflow, project, or life system.

## Diagnostic questions

- What breaks if this one thing fails?
- What backup is cheap now and expensive later?
- What dependency needs a fallback?
- How often should the backup be tested?

## Agent instruction

Create one backup route and schedule a test of it.

## Failure mode

Adding backup everywhere until the system becomes too heavy.

## Related

- [[inversion|Inversion]]
- [[antifragility|Antifragility]]
- [[parkinsons_law|Parkinsons Law]]
