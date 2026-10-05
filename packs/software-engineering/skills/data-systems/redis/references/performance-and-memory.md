# Redis performance and memory

Optimize after identifying command mix, key count, value size, concurrency, network RTT, and latency SLOs.

- Prefer pipelining/batching when many independent commands pay repeated network round trips.
- Avoid unbounded multi-key, collection, or script operations.
- Use `SCAN`-family iteration for large keyspaces and collections instead of blocking enumeration.
- Watch for big keys, hot keys, high-cardinality structures, and large serialized blobs.
- Keep client connection counts bounded; reuse pools/connections according to the client library's concurrency model.
- Separate latency-sensitive traffic from maintenance or bulk workloads when contention becomes visible.

## Memory

- Budget for dataset, object overhead, replication buffers, client buffers, persistence/fork overhead, and fragmentation.
- Choose `maxmemory` and eviction policy deliberately; cache workloads and authoritative state need different policies.
- Do not enable eviction for data that must never disappear.
- Size TTL-heavy workloads with expiration churn in mind.

## Diagnosis

Use command latency, slow log, memory stats, keyspace stats, per-command metrics, client counts, rejected/evicted keys, and application timing together. A fast Redis command can still be slow end-to-end because of connection contention or network latency.
