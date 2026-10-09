---
name: rust-database-review
description: "Use when Rust code involves database pools, SQL, transactions, Drop cleanup, or database review."
---

# Rust Database access review

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Verify pool/connection and transaction ownership, query parameterization, cancellation, cleanup via Drop, and authorization scope.
- Review async executor behavior and partial failures; load a PostgreSQL or SQLite specialist for engine semantics.
- Treat query-plan and migration claims as evidence-backed findings.

