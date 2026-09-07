---
name: mysql-migrations
description: "Use when MySQL schema migrations, rollout order, backfills, mixed application versions, or rollback limits are in scope."
---

# MySQL Migrations

Use with `mysql-online-ddl`, `mysql-locking`, and the cross-cutting
`zero-downtime-migration` skill for live systems.

## Rules

- Prefer expand, backfill, contract when old and new application versions coexist; make each step idempotent and observable.
- Review metadata locks, table-copy or rebuild cost, default evaluation, foreign keys, index creation, replication, and backup impact.
- Define how old clients read/write during the transition, including NULL/default/dual-write behavior and generated artifacts.
- Separate reversible schema changes from irreversible data changes and record the restore or rollback boundary.
- Test interrupted, retried, partially applied, and mixed-version migrations on representative data.

