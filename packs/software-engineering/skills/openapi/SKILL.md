---
name: openapi
description: "Use when designing, generating, reviewing, validating, documenting, testing, or evolving OpenAPI contracts. Load only the references relevant to the current concern."
---

# OpenAPI

Use this domain skill as the entry point for OpenAPI contract work. Keep working context small by loading only the references needed for the task.

## Reference routing

- `auth-security-review` → `references/auth-security-review.md`
- `breaking-change-detection` → `references/breaking-change-detection.md`
- `codegen` → `references/codegen.md`
- `contract-testing` → `references/contract-testing.md`
- `design` → `references/design.md`
- `documentation` → `references/documentation.md`
- `generate-spec` → `references/generate-spec.md`
- `lint` → `references/lint.md`
- `mock-generation` → `references/mock-generation.md`
- `review` → `references/review.md`
- `sample-generation` → `references/sample-generation.md`
- `schema-governance` → `references/schema-governance.md`
- `versioning-migration` → `references/versioning-migration.md`

## Rules

- Treat the API contract as the source of truth and start from repository-local conventions and compatibility policy.
- Load the smallest set of references that covers the current contract concern.
- Combine references when work crosses concerns such as design, security, compatibility, generation, and contract testing.
- Treat `references/` as detailed guidance, not independently selectable skills.
