---
name: go-cli
description: "Use when Go code involves CLI parsing, stdin/stdout/stderr, exit codes, or signals."
---

# Go CLI

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Reuse the existing CLI parser and define stdin, stdout, stderr, exit codes, signals, and cancellation at the command boundary.
- Validate flags and environment values before work begins and keep user-facing errors free of secrets.
- Do not add a CLI framework for a small command when the standard library or existing parser is sufficient.

