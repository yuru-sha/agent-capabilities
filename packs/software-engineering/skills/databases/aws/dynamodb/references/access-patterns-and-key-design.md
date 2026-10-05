# Access patterns and key design

## Start from reads and writes

List the application's concrete operations first:

- item lookup by exact identifier;
- one-to-many listing;
- range/time-window lookup;
- reverse lookup through an alternate identifier;
- uniqueness checks;
- high-frequency counters or append-like writes;
- multi-tenant isolation requirements.

Map every important access pattern to a primary-key or index query before choosing a schema.

## Partition key

Choose partition-key values that spread request volume across many logical values. Low-cardinality keys such as status, country, tenant tier, or a single constant can create hot partitions even when total table capacity is sufficient.

For bursty high-write entities, consider deterministic or random write sharding only when the corresponding read fan-out is acceptable.

## Sort key

Use sort keys to colocate related items and express efficient range queries. Composite sort-key prefixes can encode hierarchy, type, state, time, or version when that structure directly supports an access pattern.

Keep delimiter and encoding conventions stable. Avoid schema tricks that save one index at the cost of making invariants or queries opaque.

## Single-table design

Single-table design is optional, not a goal by itself. Use it when colocating multiple entity types materially reduces request count or supports transactional/query requirements. Prefer multiple tables when lifecycle, ownership, scaling, backup, authorization, or operational boundaries are clearer that way.

Document each entity's item shape, key template, access patterns, and invariant. Do not infer relationships from undocumented string conventions.
