---
name: postgresql-backup-restore
description: "Use when reviewing PostgreSQL backups, WAL archiving, point-in-time recovery, restore procedures, RPO/RTO, or disaster recovery."
---

# PostgreSQL Backup and Restore

Use with `postgresql-replication-ha`, `postgresql-migrations`, and
`postgresql-roles-rls` where access affects recovery.

## Check

- Distinguish logical, physical, base, and WAL backups and map each to the stated RPO/RTO and failure scenarios.
- Verify backup consistency, encryption, retention, access control, extension/schema/version compatibility, and monitoring of failed or stale archives.
- Perform a restore drill into an isolated environment; validate application behavior, permissions, sequences, extensions, and data completeness.
- Check point-in-time target selection, recovery configuration, replay gaps, and the procedure for promotion or rollback.
- Treat “backup completed” as insufficient evidence until a restore has been verified.

