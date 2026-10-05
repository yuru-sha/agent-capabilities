---
name: aws-secrets-manager
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Secrets Manager secrets, rotation, versions/staging labels, resource policies, caching, cross-account access, or secret delivery to workloads."
---

# aws-secrets-manager

Use this skill for secret storage, retrieval, rotation, policy, and lifecycle.

## Reference routing

- `secret-model-access-and-caching` → `references/secret-model-access-and-caching.md`
- `rotation-versions-and-recovery` → `references/rotation-versions-and-recovery.md`
- `policies-encryption-and-operations` → `references/policies-encryption-and-operations.md`

## Rules

- Store only secrets; keep non-secret configuration in a more appropriate configuration system.
- Grant retrieval to the workload identity that needs the secret and no broader.
- Cache retrieved secrets when appropriate to reduce latency/cost, but define refresh after rotation.
- Treat versions and staging labels as lifecycle state, not opaque implementation detail.
- Design rotation with application compatibility and rollback/recovery.
- Validate resource policies and cross-account exposure; avoid broadly accessible policies.
- Treat `references/` as detailed guidance, not independently selectable skills.
