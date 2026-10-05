# Ingestion, streaming, and export

Choose batch load, Storage Write API, streaming, external tables, or transfer services from latency, throughput, source, and cost requirements.

For near-real-time ingestion, define deduplication keys, retry semantics, late-arriving updates, and ordering assumptions. Do not assume producer retry means exactly-once business effects.

Use staging tables for large backfills or schema-changing loads when validation and rollback matter.

For exports, account for destination format, sharding, compression, region/location compatibility, and downstream atomicity.

Validate row counts, partition coverage, schema, and freshness after large loads or exports instead of treating job success alone as data correctness.
