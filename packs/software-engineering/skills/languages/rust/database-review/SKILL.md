---
name: rust-database-review
description: "Use when Rust code involves database pools, SQL, transactions, Drop cleanup, or database review."
---

# Rust Database access review

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Rust-specific decisions for this concern.

## Rules

- Verify pool/connection and transaction ownership, query parameterization, cancellation, cleanup via Drop, and authorization scope.
- Review async executor behavior and partial failures; load a PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings.

