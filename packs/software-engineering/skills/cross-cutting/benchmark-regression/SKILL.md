---
name: benchmark-regression
description: "Use when performance claims, benchmark baselines, allocation or latency regressions, query plans, or resource budgets are part of a change."
---

# Benchmark Regression

Compose with the language/database performance skill and the repository's
actual benchmark command.

## Check

- Record workload, input distribution, environment, toolchain, warm-up, repetitions, and baseline revision.
- Separate throughput, latency percentiles, allocations, memory, I/O, query-plan shape, and startup cost; do not collapse them into one score.
- Use repeated measurements and noise-aware thresholds; avoid optimizing a microbenchmark that does not represent the contract.
- Compare before/after artifacts and identify whether the result is code, data, cache, planner, compiler, or environment driven.
- Report the exact command and evidence, including when hardware or CI noise prevents a reliable conclusion.

