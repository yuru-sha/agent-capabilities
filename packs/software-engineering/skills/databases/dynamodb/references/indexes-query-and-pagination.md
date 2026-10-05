# Indexes, query, and pagination

## Global secondary indexes

Use a GSI when an important access pattern cannot be served by the table primary key. Define:

- index partition and sort keys;
- projection requirements;
- expected read/write rate;
- cardinality and skew;
- backfill/migration plan;
- whether eventual consistency is acceptable.

GSI reads are eventually consistent. A GSI also adds write amplification and can become the throughput bottleneck independently of the base table.

## Local secondary indexes

Use an LSI only when the same partition key with an alternate sort key is known at table creation time and its partition-size/operational constraints are acceptable. Do not choose an LSI merely to avoid adding a GSI later.

## Query versus Scan

Prefer `Query` with key conditions. Filter expressions do not reduce the read work performed before filtering, so they are not a substitute for key design.

Treat `Scan` as a bounded exception for maintenance, migration, export-like workflows, or genuinely small tables. Use segmentation and throttling when parallel scans are necessary.

## Pagination

Treat `LastEvaluatedKey` as an opaque continuation token derived from the complete key state. Do not infer completion from page size alone.

When exposing pagination externally, encode the continuation state safely and bind it to any filters/sort semantics needed to prevent accidental reuse across incompatible queries.
