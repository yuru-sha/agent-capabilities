---
name: openapi-versioning-migration
description: "Use when versioning or migrating OpenAPI contracts and planning compatible API rollouts."
---

# OpenAPI Versioning and migration

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Establish the baseline, OpenAPI version, consumer population, and deprecation policy before choosing a migration.
- Prefer additive rollout: introduce the new shape, support old and new, migrate consumers, then remove the old contract.
- Review mixed-version behavior, generated clients, examples, telemetry, and rollback limits.

