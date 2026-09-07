---
name: python3-performance
description: "Use when Python 3 code involves profiling, benchmarks, I/O, imports, serialization, or allocations."
---

# Python 3 Performance

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Measure with the repository's profiler or benchmark command before changing an algorithm; check N+1 I/O, imports, serialization, and allocations.
- Prefer bounded queues and simple data flow over speculative caches or worker pools.
- Record the workload, Python version, and command behind performance evidence.

