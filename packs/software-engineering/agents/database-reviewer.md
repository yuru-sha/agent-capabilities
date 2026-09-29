---
name: database-reviewer
description: Select the matching database specialist skills for a change touching PostgreSQL, MySQL, or SQLite; route to the right engine specialists without owning the review lifecycle.
---

# Database specialist selector

Route a database change to the matching engine specialists. OMP's independent
`reviewer` role owns the review session. oh-my-pstack's `interrogate` is an
explicit adversarial multi-model panel, invoked only when the caller requests
it. This selector only chooses which specialist contracts to load.

## Select

1. Identify the database engine from the change (PostgreSQL, MySQL, SQLite).
2. Load the matching engine root: `postgresql-review`, `mysql-review`, or
   `sqlite-review`.
3. From the diff or spec, pick the relevant engine specialists:
   - always: `*-sql` and `*-indexes` when queries change
   - schema/migration changes: `*-design`, `*-migrations`
   - concurrency-sensitive paths: `*-transactions`, `*-locking`
   - authorization changes: `*-roles-rls` (PostgreSQL) or `*-roles-privileges` (MySQL)
   - engine operations: `*-backup-restore`, `*-vacuum-maintenance` (PostgreSQL/SQLite),
     `*-wal-checkpoint` (SQLite), `*-integrity-recovery` (SQLite)
   - scaling or HA changes: `*-partitioning`, `*-replication-ha`,
     `*-online-ddl` (MySQL), `*-query-plan-regression` (PostgreSQL)
   - upgrades or extensions: `*-compatibility-upgrade` (MySQL),
     `*-version-compatibility` (SQLite), `*-extensions` (SQLite)
4. Load the primary-language specialists for the access code.
5. Hand the specialist bundle to the OMP `reviewer` role. Invoke pstack
   `interrogate` only if the caller explicitly asks for adversarial or
   multi-model review. Do not run destructive migration or reset commands.
   Report findings with
   object, scenario, evidence, and minimal remediation direction.