---
name: mysql-indexes
description: "Use when MySQL indexes, InnoDB primary keys, covering access, generated-column indexes, or index changes are designed or reviewed."
---

# MySQL Indexes

Use with `mysql-performance`, `mysql-sql`, and `mysql-online-ddl` when an index
is added or changed.

## Check

- Treat the InnoDB primary key as the clustered row identity and account for its width in every secondary index.
- Check leftmost-prefix use, selectivity, covering behavior, ordering, collation, prefix length, generated/functional expressions, and redundant indexes.
- Use representative data and parameters with `EXPLAIN` or `EXPLAIN ANALYZE`; verify estimates, access path, rows examined, and sort/temp work.
- Consider write amplification, buffer-pool cost, duplicate uniqueness semantics, and online build duration before adding an index.
- Test NULL, Unicode, case/collation, range, pagination, and mixed-version migration behavior.

