---
name: mysql-sql
description: "Use when MySQL SQL, query semantics, SQL modes, null handling, upserts, or dialect-specific behavior is in scope."
---

# MySQL SQL

Use with `mysql-indexes`, `mysql-transactions`, and the primary-language database
access skill.

## Check

- Review strict SQL modes, `ONLY_FULL_GROUP_BY`, reserved words, implicit conversions, collation comparisons, and `NULL` semantics against the deployment configuration.
- Prefer parameterized statements and make `ORDER BY` explicit whenever result order is part of the contract.
- Distinguish `INSERT ... ON DUPLICATE KEY UPDATE`, `INSERT IGNORE`, and `REPLACE`; their conflict, warning, delete, and trigger behavior differs.
- Check affected-row semantics, generated/default values, `LAST_INSERT_ID`, warnings, and driver mapping rather than assuming a successful statement proves the intended write.
- Test the actual MySQL version and connector with empty, duplicate, invalid, timezone, Unicode, and boundary values.

