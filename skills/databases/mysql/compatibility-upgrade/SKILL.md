---
name: mysql-compatibility-upgrade
description: "Use when MySQL server upgrades, connector compatibility, SQL modes, authentication changes, collations, or version support are involved."
---

# MySQL Compatibility and Upgrade

Use with `mysql-review`, `mysql-backup-restore`, `mysql-replication-ha`, and
`package-release-compatibility` for application releases.

## Check

- Define the supported server, connector, storage-engine, OS, charset/collation, and SQL-mode matrix; do not infer compatibility from one local server.
- Run the version-appropriate upgrade checker or equivalent checks for reserved words, removed/deprecated features, data types, system tables, and configuration.
- Test authentication/TLS, `lower_case_table_names`, timezone, warning/error behavior, `ONLY_FULL_GROUP_BY`, and optimizer-plan changes.
- Exercise logical/physical upgrade, rolling replication upgrade, rollback, backup restore, and mixed-version application traffic in a test environment.
- Record exact versions and unresolved incompatibilities; do not promise downgrade support without a tested path.

