---
name: go-performance
description: "Use when Go code involves benchmarks, pprof, allocations, latency, or throughput."
---

# Go Performance

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Measure with benchmarks or pprof before changing a hot path; inspect allocations and repeated I/O rather than guessing.
- Prefer simple data structures and bounded concurrency over speculative pools or caches.
- Record the workload and command behind any performance claim.

