# BullMQ queue and job design

- Use queues as explicit asynchronous boundaries with clear ownership.
- Keep job payloads small, versioned, and free of unnecessary secrets or large binaries; store large objects elsewhere and pass stable references.
- Define a stable job name and payload contract so workers can validate before side effects.
- Use deterministic/custom job IDs when deduplication semantics require it, but do not confuse deduplication with exactly-once execution.
- Decide retention with `removeOnComplete` and `removeOnFail`; unlimited retained jobs can become an operational problem.
- Keep queue names stable and environment-scoped.
- Use `QueueEvents` for cross-worker event observation rather than assuming a local Worker event sees the whole fleet.
- Separate independent workloads when they require different concurrency, rate limits, retention, or failure policies.
