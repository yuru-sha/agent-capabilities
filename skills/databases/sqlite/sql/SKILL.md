---
name: sqlite-sql
description: "Use when SQLite work involves SQL, query semantics, and database access."
---

# SQLite SQL

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Parameterize values and make null, ordering, pagination, collation, and text comparison behavior explicit.
- Do not assume server roles, parallel writers, or row order that SQLite does not provide.
- Review SQL for authorization scope, transaction state, busy behavior, and compatibility with the actual SQLite version.

