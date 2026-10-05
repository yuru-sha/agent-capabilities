---
name: sqlite
description: "Use when designing, implementing, reviewing, operating, or troubleshooting SQLite. Load only the references relevant to the current concern."
---

# SQLite

Use this domain skill as the entry point for SQLite work. Keep working context small by loading only the references needed for the task.

## Reference routing

- `backup-restore` → `references/backup-restore.md`
- `design` → `references/design.md`
- `extensions` → `references/extensions.md`
- `indexes` → `references/indexes.md`
- `integrity-recovery` → `references/integrity-recovery.md`
- `locking` → `references/locking.md`
- `migrations` → `references/migrations.md`
- `performance` → `references/performance.md`
- `review` → `references/review.md`
- `sql` → `references/sql.md`
- `transactions` → `references/transactions.md`
- `vacuum-maintenance` → `references/vacuum-maintenance.md`
- `version-compatibility` → `references/version-compatibility.md`
- `wal-checkpoint` → `references/wal-checkpoint.md`

## Rules

- Start with repository-local schema, migrations, configuration, workload assumptions, and existing conventions.
- Load the smallest set of references that covers the current database concern.
- Preserve SQLite-specific semantics rather than substituting similarly named guidance from another database engine.
- Treat `references/` as detailed guidance, not independently selectable skills.
