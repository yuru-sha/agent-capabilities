---
name: ec2
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon EC2 instances, AMIs, instance types, EBS, IMDS, placement, Auto Scaling integration, lifecycle, or host-level reliability."
---

# Amazon EC2

Use this skill for EC2 instance and host lifecycle. Use VPC, EBS/storage, Auto Scaling, or load-balancer Skills for deeper service-specific behavior when available.

## Reference routing

- `instance-ami-and-bootstrap` → `references/instance-ami-and-bootstrap.md`
- `storage-networking-and-metadata` → `references/storage-networking-and-metadata.md`
- `capacity-lifecycle-and-operations` → `references/capacity-lifecycle-and-operations.md`

## Rules

- Choose instance family, size, architecture, and purchase model from measured workload requirements.
- Treat AMIs and bootstrap/user data as versioned deployment artifacts.
- Require IMDSv2 unless a documented compatibility constraint prevents it.
- Keep instance role, network exposure, storage encryption, patching, and logging explicit.
- Design graceful replacement rather than in-place manual repair for autoscaled fleets.
- Treat Spot interruption and instance retirement as normal lifecycle events where used.
- Treat `references/` as detailed guidance, not independently selectable skills.
