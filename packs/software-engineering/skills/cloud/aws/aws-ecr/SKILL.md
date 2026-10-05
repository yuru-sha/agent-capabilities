---
name: aws-ecr
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon ECR repositories, image push/pull, tag immutability, scanning, lifecycle policies, replication, registry permissions, or container supply-chain controls."
---

# aws-ecr

Use this skill for container image registry behavior and lifecycle.

## Reference routing

- `repositories-tags-and-artifacts` → `references/repositories-tags-and-artifacts.md`
- `scanning-lifecycle-and-replication` → `references/scanning-lifecycle-and-replication.md`
- `permissions-pull-and-operations` → `references/permissions-pull-and-operations.md`

## Rules

- Prefer immutable deployment references and enable tag immutability when mutable tags are unsafe.
- Separate build/push authority from runtime pull authority.
- Define vulnerability scanning and finding ownership.
- Use lifecycle policies to control unreferenced/old artifacts without deleting rollback-critical images.
- Treat cross-Region/account replication and pull-through cache as explicit distribution choices.
- Keep image provenance/signing policy aligned with the delivery pipeline.
- Treat `references/` as detailed guidance, not independently selectable skills.
