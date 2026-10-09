---
name: go
description: "Use when implementing, reviewing, debugging, or maintaining Go code. Load only the references relevant to the current concern."
---

# Go

Use this domain skill as the entry point for Go work. Keep working context small: load only the reference files needed for the task instead of reading every reference eagerly.

Use this skill with the project's TDD workflow for implementation and its review workflow for review where applicable. Independently selectable cross-cutting capabilities should be combined with this skill when required.

## Reference routing

- `api-client` → `references/api-client.md`
- `api-compatibility` → `references/api-compatibility.md`
- `cli` → `references/cli.md`
- `code-generation` → `references/code-generation.md`
- `concurrency` → `references/concurrency.md`
- `configuration` → `references/configuration.md`
- `data-race-check` → `references/data-race-check.md`
- `database-review` → `references/database-review.md`
- `dependencies` → `references/dependencies.md`
- `documentation` → `references/documentation.md`
- `error-handling` → `references/error-handling.md`
- `fuzzing` → `references/fuzzing.md`
- `goroutine-leak-deadlock-check` → `references/goroutine-leak-deadlock-check.md`
- `http-server` → `references/http-server.md`
- `idiomatic-code-check` → `references/idiomatic-code-check.md`
- `logging` → `references/logging.md`
- `networking` → `references/networking.md`
- `observability` → `references/observability.md`
- `performance` → `references/performance.md`
- `refactoring` → `references/refactoring.md`
- `resource-management` → `references/resource-management.md`
- `security` → `references/security.md`
- `serialization` → `references/serialization.md`
- `struct-json-tags` → `references/struct-json-tags.md`
- `testing` → `references/testing.md`

## Rules

- Start with repository-local conventions, toolchain configuration, and existing patterns before applying generic guidance.
- Load the smallest set of references that covers the changed behavior; add another reference only when the task crosses that concern.
- Preserve Go-specific semantics rather than substituting similarly named guidance from another language.
- Treat files under `references/` as detailed guidance for this skill, not as independently selectable skills.
