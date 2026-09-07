---
name: sqlite-review
description: "Use when SQLite work involves database review of correctness, security, and operations."
---

# SQLite Review

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Review parameterization, foreign keys, constraints, authorization scope, connection cleanup, transaction boundaries, and busy/error handling.
- Flag assumptions about PostgreSQL features, parallel writers, server-side roles, or incidental row order.
- Separate measured facts, engine behavior, code-path inference, and unrun checks.

