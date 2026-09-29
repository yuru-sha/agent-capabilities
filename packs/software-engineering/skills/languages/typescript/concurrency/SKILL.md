---
name: typescript-concurrency
description: "Use when TypeScript or Node/browser code involves Promises, AbortSignal, workers, timers, or shared mutable state."
---

# TypeScript Concurrency

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Use AbortSignal for cancellation where supported and state whether grouped work is fail-fast or best-effort.
- Bound concurrent promises for untrusted or large collections and keep ownership of timers, streams, workers, and mutable state explicit.
- Do not hide races with delays or an unowned singleton.

