---
name: postgresql-review
description: "Use when PostgreSQL work involves database review of correctness, security, and operations."
---

# PostgreSQL Review

Use this specialist with the primary language skill and `$code-review` when reviewing a change. It owns only engine-specific decisions for this concern.

## Rules

- Review constraints, authorization/tenant scope, parameterization, transaction boundaries, lock behavior, cleanup, and migration compatibility.
- Separate engine facts, code-path inference, and checks that were not run.
- Report the affected SQL/object, failure scenario, evidence, and smallest safe remediation.

