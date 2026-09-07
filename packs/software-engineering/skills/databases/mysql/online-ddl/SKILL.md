---
name: mysql-online-ddl
description: "Use when MySQL ALTER TABLE, InnoDB online DDL, ALGORITHM/LOCK clauses, metadata locks, or live index changes are involved."
---

# MySQL Online DDL

Use with `mysql-locking`, `mysql-migrations`, and `mysql-performance`.

## Check

- Verify the actual `ALGORITHM` and `LOCK` behavior for the target MySQL version, storage engine, operation, and index/table definition.
- Plan for metadata locks at the beginning and end, active transactions, concurrent DML, replication lag, temporary disk, and online-log limits.
- Make progress, timeout, cancellation, rollback, and operator-abort behavior observable before production execution.
- Test duplicate/NULL violations, foreign keys, generated columns, partitioned tables, and failure at each DDL phase.
- Treat “online” as reduced blocking, not as a guarantee of zero locks or zero resource impact.

