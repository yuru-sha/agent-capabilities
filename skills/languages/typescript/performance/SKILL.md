---
name: typescript-performance
description: "Use when TypeScript or Node/browser code involves profiling, event-loop latency, bundle size, serialization, or repeated I/O."
---

# TypeScript Performance

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Profile the actual browser or Node runtime before optimizing; check bundle size, serialization, event-loop blocking, and repeated I/O.
- Prefer simple data flow and bounded work over speculative memoization or worker pools.
- Record the workload and measurement command behind a performance claim.

