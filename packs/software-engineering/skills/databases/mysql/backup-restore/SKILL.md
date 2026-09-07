---
name: mysql-backup-restore
description: "Use when MySQL logical or physical backups, binary-log recovery, point-in-time restore, or disaster recovery are in scope."
---

# MySQL Backup and Restore

Use with `mysql-replication-ha`, `mysql-compatibility-upgrade`, and
`mysql-roles-privileges` where recovery access matters.

## Check

- Choose a consistent logical or physical backup and map it to RPO/RTO, dataset size, storage engine, binlogs, and topology.
- Verify backup consistency, binlog retention/position or GTID continuity, encryption, access control, retention, charset/collation, and version compatibility.
- Restore into an isolated server and validate schema, data, indexes, users/roles, routines, events, sequences/auto-increment behavior, and application reads.
- Exercise point-in-time recovery, incomplete backup, missing binlog, disk-full, and interrupted restore paths.
- Treat successful dump completion as insufficient evidence until restore and application-level verification succeed.

