---
name: sqlite-transactions
description: "Use when SQLite work involves transaction scope, isolation, and commit behavior."
---

# SQLite Transactions

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Choose deferred, immediate, or exclusive transactions based on when the writer must reserve the database.
- Keep write transactions short and make commit/rollback and connection ownership explicit.
- Review crash recovery, busy errors, cancellation, and whether retries can duplicate writes.

