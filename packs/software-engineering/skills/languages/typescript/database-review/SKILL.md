---
name: typescript-database-review
description: "Use when TypeScript or Node/browser code involves database pools, SQL, transactions, query ordering, or database review."
---

# TypeScript Database access review

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Verify parameterized SQL, pool and transaction ownership, client release in finally, timeout/cancellation, and authorization scope.
- Review asynchronous query ordering and partial-failure behavior; load a PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings.

