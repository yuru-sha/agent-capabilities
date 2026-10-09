---
name: go-refactoring
description: "Use when Go code involves package boundaries, interfaces, exported APIs, or generated code."
---

# Go Refactoring

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Keep packages cohesive and exported APIs stable; introduce an interface only when a second real implementation or test seam needs it.
- Prefer a small local refactor that clarifies ownership over a new generic helper or package layer.
- Keep generated code and hand-written adapters separate.

