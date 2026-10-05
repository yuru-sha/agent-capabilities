# BullMQ workers and concurrency

- Local Worker `concurrency` is effective for I/O-bound asynchronous jobs.
- CPU-bound processors can starve lock renewal and the Node.js event loop; use sandboxed processors or separate compute workers.
- Multiple worker processes/instances improve both concurrency and availability.
- Compute total concurrency across every replica, not just one Worker instance.
- Protect downstream databases/APIs with explicit concurrency and rate limits.
- Graceful shutdown should stop taking new jobs and await current jobs with a bounded application-level shutdown plan.
- A graceful `worker.close()` waits for active jobs; the application must still define its own overall termination deadline.
- Tune job duration, lock renewal/stalled behavior, and external timeouts together rather than independently.

When autoscaling, use queue age/backlog and downstream saturation signals instead of CPU alone.
