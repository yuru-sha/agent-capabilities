---
name: openapi-review
description: "Use when semantically reviewing an OpenAPI description beyond mechanical lint."
---

# OpenAPI Review

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Separate mechanical lint findings from semantic review of resources, authorization, statuses, data shapes, and lifecycle.
- Compare changed operations with neighboring contracts and identify missing errors, examples, security requirements, or pagination semantics.
- Cite the spec path and the requirement or consumer evidence behind each finding.

