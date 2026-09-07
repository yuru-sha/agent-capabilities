---
name: mysql-design
description: "Use when MySQL work involves schema, InnoDB data modeling, character sets, collations, or engine-specific constraints."
---

# MySQL Design

Use with the primary-language skill and `$code-review` when reviewing a change.
It owns MySQL-specific design decisions for this concern.

## Rules

- Choose storage engine, primary key shape, signedness, nullability, generated values, and foreign-key behavior deliberately.
- Set character set, collation, comparison semantics, timezone representation, and identifier case behavior explicitly at the boundary.
- Model invariants with constraints where MySQL enforces them and identify what remains an application or transaction invariant.
- Keep InnoDB clustered-key size and secondary-index consequences visible when selecting identifiers.
- Verify the target MySQL version, SQL mode, and connector behavior before relying on a feature or default.

