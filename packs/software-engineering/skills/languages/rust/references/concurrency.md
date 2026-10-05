---
name: rust-concurrency
description: "Use when Rust code involves async tasks, threads, Send/Sync, channels, locks, or cancellation."
---

# Rust Concurrency

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Rust-specific decisions for this concern.

## Rules

- Make Send/Sync bounds, ownership, lock scope, channel closure, and task lifetime explicit.
- Use the repository's async runtime and define cancellation and JoinHandle shutdown; do not spawn unowned work.
- Avoid blocking an async executor and test deadlock, cancellation, and error propagation paths.

