---
name: sqlite-migrations
description: "Use when SQLite work involves schema migrations, rollout, and compatibility."
---

# SQLite Migrations

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Treat table rebuilds, copy/transform steps, indexes, triggers, foreign keys, and schema version updates as one tested migration.
- Test the actual older schema and review mixed-version readers/writers, crash recovery, backups, and file permissions.
- State data-loss and rollback limits; do not call a destructive rebuild reversible without a restore path.

