---
name: rust-async-runtime
description: "Use when Rust async tasks, executors, cancellation, JoinHandles, blocking work, Send bounds, or runtime shutdown are involved."
---

# Rust Async Runtime

Use with `$tdd`, `rust-concurrency`, `rust-resource-management`, and the
repository's selected async runtime.

## Check

- Identify runtime ownership, task ownership, cancellation, `JoinHandle` handling, timeout, and shutdown behavior for every spawned task.
- Keep blocking I/O and CPU work off the async executor through the established boundary; make backpressure and queue limits explicit.
- Review `Send`/`Sync`, shared state, lock-across-`await`, task detachment, cancellation safety, and error propagation.
- Test cancellation, timeout, partial failure, runtime shutdown, and repeated start/stop without sleeps as the only synchronization.
- Use the repository's runtime and test utilities; do not mix executors or create hidden runtimes without a lifecycle owner.

