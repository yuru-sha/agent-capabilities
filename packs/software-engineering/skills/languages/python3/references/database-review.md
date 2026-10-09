---
name: python3-database-review
description: "Use when Python 3 code involves database connections, SQL, transactions, cleanup, or database review."
---

# Python 3 Database access review

Use the project's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Verify parameterized SQL, connection/cursor ownership, transaction scope, context-manager cleanup, timeouts, and authorization scope.
- Review async/sync boundary behavior and partial failures; load a PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings.

