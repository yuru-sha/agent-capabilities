---
name: postgresql-sql
description: "Use when PostgreSQL work involves SQL, query semantics, and database access."
---

# PostgreSQL SQL

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Parameterize values and make null semantics, ordering, pagination, time zone, and content selection explicit.
- Qualify objects where search_path ambiguity matters and return only columns required by the caller.
- Review SQL for authorization scope, N+1 access, statement timeout, and mixed-version compatibility.

