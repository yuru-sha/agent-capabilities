---
name: mysql-review
description: "Use when reviewing MySQL schema, SQL, access code, transactions, security, migrations, or operations for correctness and risk."
---

# MySQL Review

Use with `$code-review` and the focused MySQL specialists for the concerns in
the diff. It is a review lens, not a replacement for those specialists.

## Check

- Review parameterization, SQL mode, charset/collation, constraints, index shape, transaction ownership, connection cleanup, and timeout behavior.
- Check InnoDB versus nontransactional assumptions, implicit commits, deadlocks, metadata locks, replication effects, and migration compatibility.
- Verify roles, grants, TLS/authentication, secret handling, tenant scope, backup/recovery, and operational observability where applicable.
- Distinguish measured engine behavior, application inference, version-dependent behavior, and checks that were not run.
- Report the affected object, failure scenario, evidence, and smallest remediation direction.

