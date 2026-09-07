---
name: mysql-locking
description: "Use when reviewing MySQL InnoDB record, gap, next-key, metadata, table, or deadlock behavior."
---

# MySQL Locking

Use with `mysql-transactions`, `mysql-migrations`, and `mysql-online-ddl`.

## Check

- Identify the index access path and the record, gap, next-key, intention, or metadata locks it can acquire at the chosen isolation level.
- Review lock ordering across statements and services, range predicates, missing indexes, foreign keys, and long-lived transactions for deadlock or lock amplification.
- Treat “online” DDL as potentially blocked by metadata locks; inspect initial/final lock phases and active transactions.
- Define bounded wait behavior, deadlock detection/retry safety, operator visibility, and transaction abort handling.
- Use lock-wait/deadlock evidence from supported instrumentation and reproduce contention with deterministic concurrent tests.

