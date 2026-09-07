---
name: postgresql-design
description: "Use when PostgreSQL work involves schema and data-model design."
---

# PostgreSQL Design

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Model invariants with NOT NULL, CHECK, foreign keys, unique constraints, and explicit delete/update behavior.
- Choose types, time zones, collations, ownership, and grants deliberately; treat search_path and SECURITY DEFINER as security boundaries.
- Keep tenant/resource scope visible in the schema and review whether application-only invariants can be violated by another writer.

