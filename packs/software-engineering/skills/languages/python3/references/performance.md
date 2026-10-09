---
name: python3-performance
description: "Use when Python 3 code involves profiling, benchmarks, I/O, imports, serialization, or allocations."
---

# Python 3 Performance

Use the project's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Measure with the repository's profiler or benchmark command before changing an algorithm; check N+1 I/O, imports, serialization, and allocations.
- Prefer bounded queues and simple data flow over speculative caches or worker pools.
- Record the workload, Python version, and command behind performance evidence.

