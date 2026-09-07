---
name: openapi-generate-spec
description: "Use when generating OpenAPI specifications from code, annotations, or requirements and checking drift."
---

# OpenAPI Spec generation

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Identify the authoritative source before generating: hand-authored spec, annotations, code, or a checked-in generated artifact.
- Make generation deterministic, preserve the chosen OpenAPI version, and compare generated output for drift.
- Do not edit generated output as the source of truth; change the source or generator configuration.

