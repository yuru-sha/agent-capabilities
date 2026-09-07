---
name: openapi-breaking-change-detection
description: "Use when detecting breaking or potentially breaking changes between OpenAPI contract versions."
---

# OpenAPI Breaking-change detection

Use this specialist with the repository's selected OpenAPI version, source of truth, and existing tools. Pair it with the matching language/database specialist when implementation behavior is in scope.

## Rules

- Compare against an explicit baseline and classify endpoint/method removal, response property removal, required-property addition, and type/nullability changes.
- Also review enum removal, incompatible status/content-type changes, stricter validation, security tightening, and pagination changes.
- Report consumer evidence and distinguish confirmed breaking changes, potentially breaking changes, and unknown impact.

