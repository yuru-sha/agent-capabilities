---
name: go-concurrency
description: "Use when Go code involves goroutines, channels, cancellation, workers, or shared state."
---

# Go Concurrency

Use this specialist with oh-my-pstack's TDD workflow for implementation and oh-my-pstack's review workflow for review. It owns only Go-specific decisions for this concern.

## Rules

- Carry context.Context from the boundary and define ownership and shutdown for every goroutine, worker, timer, and channel.
- Make channel-close responsibility explicit, bound worker counts, and test cancellation and error paths for leaks.
- Keep shared state synchronization local and visible; do not hide races behind sleeps.

