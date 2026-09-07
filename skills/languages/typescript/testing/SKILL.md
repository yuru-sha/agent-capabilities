---
name: typescript-testing
description: "Use when TypeScript or Node/browser code involves tests, async assertions, fake timers, snapshots, or type checking."
---

# TypeScript Testing

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Use the repository's existing test runner and type checker; test public behavior, rejected promises, aborts, and cleanup at the boundary.
- Use fake timers, HTTP helpers, and snapshots only when they are already part of the project and do not restate implementation.
- Keep async tests deterministic and independent of event-loop timing.

