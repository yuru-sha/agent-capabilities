---
name: typescript-cli
description: "Use when TypeScript or Node/browser code involves CLI parsing, streams, exit codes, signals, or command errors."
---

# TypeScript CLI

Use this specialist with pstack's TDD workflow for implementation and pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Reuse the existing CLI layer and define argv, stdin, stdout, stderr, exit codes, signals, and cancellation at the boundary.
- Render user-safe errors without leaking stacks or credentials and validate configuration before side effects.
- Do not add a CLI framework for a small command when the runtime or existing project code is enough.

