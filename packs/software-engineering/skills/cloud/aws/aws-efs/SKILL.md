---
name: aws-efs
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon EFS file systems, mount targets, access points, performance or throughput modes, lifecycle storage classes, encryption, backups, NFS permissions, or shared filesystem reliability."
---

# aws-efs

Use this skill for efs-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- filesystem-networking-and-access -> references/filesystem-networking-and-access.md
- performance-throughput-lifecycle-and-operations -> references/performance-throughput-lifecycle-and-operations.md

## Rules

- Create mount targets according to client AZ topology.
- Treat security groups, NFS permissions, POSIX identity, and access points together.
- Prefer General Purpose performance mode for new workloads unless justified.
- Choose throughput mode from measured workload behavior.
- Treat lifecycle storage classes and backup separately from multi-AZ availability.
- Treat references/ as detailed guidance, not independently selectable skills.
