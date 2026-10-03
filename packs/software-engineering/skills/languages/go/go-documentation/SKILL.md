---
name: go-documentation
description: "Use when Go code involves package docs, API examples, CLI help, or compatibility documentation."
---

# Go Documentation

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Keep exported package, type, and function docs, API examples, CLI help, and error behavior aligned with the implementation.
- Prefer a small runnable example over a broad promise that no check verifies.
- Document compatibility and failure boundaries where users must make a decision.

