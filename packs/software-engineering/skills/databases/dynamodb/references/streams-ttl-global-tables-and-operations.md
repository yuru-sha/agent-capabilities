# Streams, TTL, global tables, and operations

## DynamoDB Streams

Use Streams when downstream processing must react to item-level changes. Consumers must tolerate duplicate delivery and replay. Make event filtering, ordering assumptions, checkpoint ownership, failure handling, and replay procedures explicit.

With Lambda event source mappings, design for partial failures and poison records rather than relying on all-or-nothing retries of large batches.

## TTL

TTL is asynchronous expiration, not an exact scheduler. Do not depend on an item disappearing at a precise instant for authorization, billing, locking, or correctness.

If immediate semantic expiry matters, check the expiry attribute in application logic even when TTL is enabled.

## Global tables

Use global tables only when multi-Region active access or locality requirements justify replication complexity. Define conflict expectations, consistency model, Region-failure behavior, and failover/failback procedures.

Do not assume cross-Region transactional atomicity. Validate application invariants under concurrent writes from multiple Regions.

## Backup and recovery

Enable point-in-time recovery or backup policies according to recovery objectives. Test restores into a separate table and document how applications, indexes, Streams, TTL, and integrations are reconciled after recovery.

## Security and observability

Use least-privilege IAM, encryption requirements appropriate to the workload, and metrics/alarms for throttling, latency, errors, consumed/provisioned capacity, and replication/stream backlogs where applicable.
