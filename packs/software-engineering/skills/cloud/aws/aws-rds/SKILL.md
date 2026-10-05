---
name: aws-rds
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon RDS/Aurora instances or clusters, backups, Multi-AZ, read replicas, parameter groups, failover, RDS Proxy, IAM auth, or database connectivity."
---

# aws-rds

Use this skill for managed relational database infrastructure. Compose it with the engine-specific database Skill for SQL, transaction, schema, and engine behavior.

## Reference routing

- `topology-availability-and-recovery` → `references/topology-availability-and-recovery.md`
- `connectivity-auth-and-configuration` → `references/connectivity-auth-and-configuration.md`
- `performance-scaling-and-operations` → `references/performance-scaling-and-operations.md`

## Rules

- Separate RDS/Aurora infrastructure behavior from engine-specific database semantics.
- Design Multi-AZ, replicas, backups/PITR, and failover from RTO/RPO and read-scaling requirements.
- Keep DB subnets private and constrain security groups to known callers.
- Treat parameter/option groups as versioned configuration with reboot/failover impact.
- Bound application connections and use pooling/RDS Proxy when workload patterns justify it.
- Test restore and failover paths; provisioning success is not recovery evidence.
- Treat `references/` as detailed guidance, not independently selectable skills.
