# Redis operations and security

## Production controls

- Bind/expose Redis only on intended networks.
- Use ACLs with least privilege; avoid sharing an all-powerful credential across services.
- Use TLS where network trust boundaries require it.
- Keep secrets out of source control and logs.
- Disable or restrict dangerous administrative capabilities according to deployment model.

## Observability

Track at least:

- memory usage, fragmentation, evictions, expirations;
- connected/blocked clients and connection failures;
- command latency and slow log;
- replication lag/state and failover events;
- persistence errors and rewrite/snapshot health;
- keyspace hit/miss rate when Redis is used as a cache.

## Operational safety

- Prefer `UNLINK` or bounded deletion strategies for very large values when synchronous deletion could hurt latency.
- Avoid bulk maintenance on the critical path.
- Test upgrades for persistence compatibility, client behavior, and module/command changes.
- Separate application errors from Redis saturation, network faults, and topology changes in diagnostics.
