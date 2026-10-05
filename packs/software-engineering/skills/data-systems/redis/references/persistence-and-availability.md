# Redis persistence and availability

Durability is a workload decision, not a default property.

## Persistence

- RDB favors compact snapshots and fast restarts but can lose writes since the last snapshot.
- AOF records writes and can reduce data-loss windows at higher write and storage cost depending on fsync policy.
- Combined persistence can be appropriate when recovery goals justify it.
- Validate backup and restore procedures; replication is not a backup.

## Availability

- Replication provides copies but does not by itself provide safe automatic failover.
- Sentinel is appropriate for non-clustered primary/replica failover.
- Redis Cluster adds sharding and failover with slot-based constraints and operational complexity.
- During failover, reconnects, retries, stale reads, and ambiguous writes must be considered explicitly.

## Rules

- Define RPO/RTO and test against them.
- Make read-from-replica consistency assumptions explicit.
- Do not assume acknowledged writes are immune to loss across every failover configuration.
- Plan client behavior for topology changes, MOVED/ASK redirection where relevant, DNS/service discovery, and retry storms.
