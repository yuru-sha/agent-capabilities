# Redis data model and keys

Use Redis structures from the access pattern outward.

- Strings fit counters, tokens, cached blobs, leases, and simple values.
- Hashes fit bounded object-like records when field-level updates matter.
- Sets and sorted sets fit membership, ranking, scheduling indexes, and deduplication indexes.
- Lists fit simple ordered queues, but use Streams when consumer groups, acknowledgements, replay, and delivery tracking are required.
- Streams are not a substitute for every queue; choose them when log-like replay and multiple consumers are part of the contract.
- HyperLogLog, bitmaps, and geospatial structures are specialized tools; use them only when their approximation or indexing model matches the requirement.

## Key design

- Namespace keys by domain and tenant where isolation is needed.
- Keep key names stable, inspectable, and bounded in length.
- Avoid accidental hot keys by considering write fan-in and read fan-out.
- For Cluster, use hash tags only when multi-key atomicity or co-location is intentional.
- Store version/schema information when serialized payload shape can evolve.

## Expiration

- Define which keys are immortal, which have TTLs, and who owns refresh.
- Avoid synchronized expiry storms; add jitter when many keys are populated together.
- For cache-aside, plan for cold misses, stampedes, negative caching, and stale-data tolerance.
- Do not rely on TTL alone for business correctness when state transitions require durable confirmation.
