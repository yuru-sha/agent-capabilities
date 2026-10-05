# Query performance and cost

Project only required columns and filter partitions early. Avoid repeated full scans of large raw tables when a curated/materialized layer can serve stable workloads.

Inspect query plan stages, bytes processed, shuffle, skew, and slot consumption when optimizing.

Prefer approximate functions only when their error bounds satisfy the use case.

Use materialized views, result caching, scheduled tables, or incremental transformations when they reduce repeated expensive work.

Reservations/editions/slot commitments should reflect concurrency and workload classes rather than a single peak query.

Set query limits, labels, budgets, and workload ownership so runaway analytical queries are attributable and controllable.
