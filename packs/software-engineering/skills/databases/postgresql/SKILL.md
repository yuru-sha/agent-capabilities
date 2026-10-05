---
name: postgresql
description: "Use when designing, implementing, reviewing, operating, or troubleshooting PostgreSQL. Load only the references relevant to the current concern."
---

# PostgreSQL

Use this domain skill as the entry point for PostgreSQL work. Keep working context small by loading only the references needed for the task.

## Reference routing

- `backup-restore` → `references/backup-restore.md`
- `design` → `references/design.md`
- `indexes` → `references/indexes.md`
- `locking` → `references/locking.md`
- `migrations` → `references/migrations.md`
- `partitioning` → `references/partitioning.md`
- `performance` → `references/performance.md`
- `query-plan-regression` → `references/query-plan-regression.md`
- `replication-ha` → `references/replication-ha.md`
- `review` → `references/review.md`
- `roles-rls` → `references/roles-rls.md`
- `sql` → `references/sql.md`
- `transactions` → `references/transactions.md`
- `vacuum-maintenance` → `references/vacuum-maintenance.md`

## Rules

- Start with repository-local schema, migrations, configuration, workload assumptions, and existing conventions.
- Load the smallest set of references that covers the current database concern.
- Preserve PostgreSQL-specific semantics rather than substituting similarly named guidance from another database engine.
- Treat `references/` as detailed guidance, not independently selectable skills.
