---
name: mysql
description: "Use when designing, implementing, reviewing, operating, or troubleshooting MySQL. Load only the references relevant to the current concern."
---

# MySQL

Use this domain skill as the entry point for MySQL work. Keep working context small by loading only the references needed for the task.

## Reference routing

- `backup-restore` → `references/backup-restore.md`
- `compatibility-upgrade` → `references/compatibility-upgrade.md`
- `design` → `references/design.md`
- `indexes` → `references/indexes.md`
- `locking` → `references/locking.md`
- `migrations` → `references/migrations.md`
- `online-ddl` → `references/online-ddl.md`
- `partitioning` → `references/partitioning.md`
- `performance` → `references/performance.md`
- `replication-ha` → `references/replication-ha.md`
- `review` → `references/review.md`
- `roles-privileges` → `references/roles-privileges.md`
- `sql` → `references/sql.md`
- `transactions` → `references/transactions.md`

## Rules

- Start with repository-local schema, migrations, configuration, workload assumptions, and existing conventions.
- Load the smallest set of references that covers the current database concern.
- Preserve MySQL-specific semantics rather than substituting similarly named guidance from another database engine.
- Treat `references/` as detailed guidance, not independently selectable skills.
