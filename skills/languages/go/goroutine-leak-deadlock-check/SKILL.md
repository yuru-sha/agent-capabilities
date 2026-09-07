---
name: go-goroutine-leak-deadlock-check
description: "Use when reviewing Go concurrency for goroutine leaks, blocked shutdown, channel deadlocks, lock-order problems, or WaitGroup misuse."
---

# Go Goroutine Leak and Deadlock Check

Use with `$tdd`, `go-concurrency`, `go-resource-management`, and
`go-data-race-check` when relevant. This skill is a liveness review, not a
replacement for the race detector.

## Check

- Trace ownership, start conditions, cancellation, exit conditions, and joins for every goroutine, worker, timer, and channel.
- Look for blocked sends/receives, forgotten channel closes, `WaitGroup` ordering mistakes, unbounded fan-out, and `select` paths that cannot make progress.
- Inspect lock ordering, nested locks, callbacks while holding locks, and error paths that return without releasing a resource.
- Exercise cancellation, timeout, server shutdown, partial failure, and repeated start/stop paths with deterministic barriers rather than sleeps.
- Report the concrete blocked path or leak evidence; state which paths were not exercised.

