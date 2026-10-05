---
name: aws-architecture
description: "Use when designing or reviewing cross-service AWS architecture, account/Region/AZ boundaries, availability, disaster recovery, network/data trust boundaries, service selection, ownership, or failure paths."
---

# AWS architecture

Use this skill for cross-service AWS architecture decisions. Keep service-specific implementation details in the corresponding service Skill.

## Reference routing

- `boundaries-and-topology` → `references/boundaries-and-topology.md`
- `availability-and-recovery` → `references/availability-and-recovery.md`
- `service-selection-and-ownership` → `references/service-selection-and-ownership.md`

## Rules

- Trace request, data, identity, and failure paths across the services in scope.
- Make account, Region, Availability Zone, environment, and public/private boundaries explicit.
- Separate control-plane, deployment, and workload-runtime responsibilities.
- Prefer service-specific Skills for configuration details; this Skill owns only cross-service composition and tradeoffs.
- Define recovery objectives, failure domains, rollback/failover ownership, and degraded-mode behavior before claiming high availability.
- Give each resource and field one infrastructure/deployment owner to avoid overlapping control planes.
- Make cost, quota, data residency, encryption, and observability consequences visible when they materially affect the architecture.
- Treat `references/` as detailed guidance, not independently selectable skills.
