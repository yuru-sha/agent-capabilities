---
name: sqlite-design
description: "Use when SQLite work involves schema and data-model design."
---

# SQLite Design

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Account for type affinity and use STRICT tables or explicit checks when flexible typing would weaken an invariant.
- Define foreign-key behavior and ensure enforcement is enabled for every connection that relies on it.
- Choose rowid, INTEGER PRIMARY KEY, WITHOUT ROWID, collation, and file ownership deliberately.

