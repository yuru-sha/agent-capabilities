# Capacity, performance, and hot partitions

## Capacity mode

Choose on-demand for variable or hard-to-predict traffic when its cost profile is acceptable. Choose provisioned capacity when workload shape is understood and explicit capacity/autoscaling control is useful.

Do not use table-level capacity as proof that every key can sustain the same traffic. Per-partition limits and skew still matter.

## Hot partitions

Look for:

- a small set of partition-key values receiving most traffic;
- monotonic or time-bucket keys that concentrate current writes;
- GSIs whose key design collapses many base-table items into a few values;
- large-item workloads consuming capacity faster than request counts suggest.

Mitigations include higher-cardinality keys, write sharding, cache/read-through design, request smoothing, or changing the access pattern.

## Item size and projections

Model item size because read/write capacity, network transfer, latency, and index storage all depend on it. Project only attributes required by index access patterns.

Avoid unbounded list/map growth inside a single item. Split append-heavy or history-like data into separate items.

## Retry and throttling

Use bounded exponential backoff with jitter for retryable throttling and transient errors. Observe returned throttling reasons and CloudWatch metrics rather than increasing retries blindly.

A retry storm can amplify a hot-partition problem; apply concurrency limits and backpressure at the caller.
