---
name: postgresql-transactions
description: "Use when PostgreSQL work involves transaction scope, isolation, and commit behavior."
---

# PostgreSQL Transactions

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Define transaction scope and isolation from the business invariant and keep network/user interaction outside the transaction.
- Make commit/rollback ownership, timeout, and cancellation explicit in application code.
- Review serialization failures, retry safety, long-running reads, and partial work at the boundary.

