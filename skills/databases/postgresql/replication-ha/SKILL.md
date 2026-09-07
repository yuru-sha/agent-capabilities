---
name: postgresql-replication-ha
description: "Use when PostgreSQL streaming or logical replication, failover, read replicas, replication slots, CDC, or high availability change."
---

# PostgreSQL Replication and HA

Use with `postgresql-backup-restore`, `postgresql-roles-rls`, and the
operational-quality skill.

## Check

- Identify physical versus logical replication, source of truth, failover trigger, promotion procedure, and data-loss boundary.
- Monitor replay/write lag, replication slots, WAL retention, disconnected consumers, conflicts, and replica freshness before routing reads.
- Define read-after-write behavior, stale-read tolerance, sequence/identity behavior, DDL and extension propagation, and CDC semantics.
- Test promotion, client reconnection, split-brain prevention, rejoin, rollback, and degraded operation instead of only steady state.
- Keep alerts tied to recovery objectives and retain evidence of the last successful failover or restore drill.

