---
name: postgresql-migrations
description: "Use when PostgreSQL work involves schema migrations, rollout, and compatibility."
---

# PostgreSQL Migrations

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Prefer expand, backfill, contract for live systems and support mixed application versions during rollout.
- Review locks, table rewrites, default evaluation, index build duration, concurrent deploys, and rollback/data-loss limits.
- Keep migrations ordered, deterministic, observable, and explicit about irreversible steps.

