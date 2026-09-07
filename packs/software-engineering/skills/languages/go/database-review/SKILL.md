---
name: go-database-review
description: "Use when Go code involves database/sql access, query boundaries, transactions, or database review."
---

# Go Database access review

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- For database/sql, verify context propagation, rows/statement/transaction cleanup, parameterization, and bounded query behavior.
- Review transaction ownership and error paths at the caller; load the PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings, not style preferences.

