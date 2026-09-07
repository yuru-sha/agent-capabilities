---
name: mysql-transactions
description: "Use when MySQL transaction scope, autocommit, isolation, commit behavior, or transactional storage-engine semantics are in scope."
---

# MySQL Transactions

Use with the primary-language database skill, `mysql-locking`, and `$code-review`.

## Rules

- Define transaction scope from the business invariant and verify that every participating table uses compatible transactional semantics.
- Make autocommit, connection-pool reuse, commit/rollback ownership, timeout, cancellation, and implicit-commit statements explicit.
- Select isolation and locking reads for the invariant; review visibility, phantom/range behavior, deadlock retries, and serialization failures.
- Keep network/user interaction and unbounded work outside the transaction; bound lock and transaction duration.
- Test partial failure, connection loss, retry/replay, duplicate delivery, and rollback of generated/default values.

