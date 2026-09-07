---
name: python3-database-review
description: "Use when Python 3 code involves database connections, SQL, transactions, cleanup, or database review."
---

# Python 3 Database access review

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Verify parameterized SQL, connection/cursor ownership, transaction scope, context-manager cleanup, timeouts, and authorization scope.
- Review async/sync boundary behavior and partial failures; load a PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings.

