---
name: mysql-replication-ha
description: "Use when MySQL replication, GTIDs, read replicas, binary logging, CDC, failover, Group Replication, or high availability changes."
---

# MySQL Replication and HA

Use with `mysql-backup-restore`, `mysql-compatibility-upgrade`, and the
operational-quality skill.

## Check

- Identify source of truth, topology, binlog format, GTID policy, replication mode, failover trigger, promotion authority, and data-loss boundary.
- Monitor apply lag, relay/binlog retention, replication errors, filters, conflicts, read-only/super-read-only state, and CDC consumers.
- Define read-after-write routing, stale-read tolerance, auto-increment/identity behavior, DDL propagation, and transaction ordering.
- Test promotion, client reconnection, split-brain prevention, rejoin, rollback, delayed replica, and degraded operation.
- Keep alerts tied to RPO/RTO and retain evidence of the last successful failover or restore drill.

