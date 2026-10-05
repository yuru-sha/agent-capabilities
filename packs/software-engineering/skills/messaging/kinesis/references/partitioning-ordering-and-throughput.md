# Partitioning, ordering, and throughput

## Partition keys

The partition key determines shard placement. Use a key that matches the smallest ordering domain the application truly requires while preserving enough cardinality to distribute load.

Avoid a single tenant, device, customer, or time bucket becoming the partition key when its traffic can exceed one shard's write capacity.

When strict per-entity order is required, do not randomize that entity's partition key merely to gain throughput; redesign the ordering domain or split the entity workload intentionally.

## Producer batching

Batch writes to reduce request overhead when latency permits. Handle per-record failures independently in batch APIs and retry only failed records with bounded backoff/jitter.

Do not allow retries to reorder application-visible effects unless the event contract permits it.

## Capacity model

Shard capacity is finite, so estimate bytes/sec and records/sec on writes and consumer read demand. Include partition-key bytes and peak/skew behavior, not only averages.

Use CloudWatch metrics and throttling signals to detect hot shards. Scaling total shard count does not automatically fix a single disproportionately hot partition key.
