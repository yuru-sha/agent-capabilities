# Table design, partitioning, and clustering

Choose table structure from query patterns and data lifecycle.

Partition by ingestion time, date/time column, or integer range when most queries can constrain that dimension. Require partition filters where accidental full scans are unacceptable.

Use clustering on high-value filter/join/grouping columns when cardinality and query shape can benefit. Do not expect clustering to replace partition pruning.

Keep partition granularity aligned with data volume and retention. Excessive tiny partitions increase metadata/operational overhead.

Use nested and repeated fields when related data is commonly consumed together and denormalization reduces expensive joins without making updates or semantics opaque.

Document table expiration, partition expiration, and historical/backfill behavior.
