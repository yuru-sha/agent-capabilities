---
name: python3-concurrency
description: "Use when Python 3 code involves asyncio, threads, processes, tasks, queues, or cancellation."
---

# Python 3 Concurrency

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Use asyncio for I/O concurrency, threads for blocking I/O when appropriate, and processes only when the workload justifies the cost.
- Define task ownership, cancellation, queue bounds, and shutdown; do not leave background tasks attached to a request.
- Account for the GIL and shared mutable state instead of assuming threads provide CPU parallelism.

