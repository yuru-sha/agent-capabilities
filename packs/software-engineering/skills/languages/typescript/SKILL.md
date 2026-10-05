---
name: typescript
description: "Use when implementing, reviewing, debugging, or maintaining TypeScript code. Load only the references relevant to the current concern."
---

# TypeScript

Use this domain skill as the entry point for TypeScript work. Keep working context small: load only the reference files needed for the task instead of reading every reference eagerly.

## Reference routing

- `api-client` → `references/api-client.md`
- `cli` → `references/cli.md`
- `concurrency` → `references/concurrency.md`
- `configuration` → `references/configuration.md`
- `data-race-check` → `references/data-race-check.md`
- `database-review` → `references/database-review.md`
- `dependencies` → `references/dependencies.md`
- `documentation` → `references/documentation.md`
- `dom-accessibility` → `references/dom-accessibility.md`
- `error-handling` → `references/error-handling.md`
- `idiomatic-code-check` → `references/idiomatic-code-check.md`
- `logging` → `references/logging.md`
- `lambda-nodejs` → `references/lambda-nodejs.md`
- `module-build` → `references/module-build.md`
- `networking` → `references/networking.md`
- `observability` → `references/observability.md`
- `package-publishing` → `references/package-publishing.md`
- `performance` → `references/performance.md`
- `refactoring` → `references/refactoring.md`
- `resource-management` → `references/resource-management.md`
- `runtime-validation` → `references/runtime-validation.md`
- `security` → `references/security.md`
- `serialization` → `references/serialization.md`
- `testing` → `references/testing.md`
- `type-design` → `references/type-design.md`

## Rules

- Start with repository-local conventions, toolchain configuration, and existing patterns.
- Load the smallest set of references that covers the changed behavior.
- Preserve TypeScript-specific semantics rather than substituting guidance from another language.
- Treat `references/` as detailed guidance, not independently selectable skills.
