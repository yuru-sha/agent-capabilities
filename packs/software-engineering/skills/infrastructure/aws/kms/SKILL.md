---
name: kms
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS KMS keys, key policies, IAM integration, grants, aliases, envelope encryption, rotation, imported material, or multi-Region keys."
---

# AWS KMS

Use this skill for KMS key authorization and cryptographic key lifecycle. Service-specific encryption behavior remains in the corresponding service Skill.

## Reference routing

- `key-policies-iam-and-grants` → `references/key-policies-iam-and-grants.md`
- `envelope-encryption-and-key-choice` → `references/envelope-encryption-and-key-choice.md`
- `rotation-multi-region-and-operations` → `references/rotation-multi-region-and-operations.md`

## Rules

- Treat the key policy as the primary KMS authorization boundary; IAM permissions alone may not be sufficient.
- Separate key administration from key usage.
- Use grants deliberately for service/workload delegation and constrain them where possible.
- Prefer envelope encryption patterns rather than sending large payloads directly to KMS.
- Choose AWS-owned, AWS-managed, or customer-managed keys from control/audit/rotation requirements.
- Treat disable/delete, imported material, and multi-Region configuration as high-impact lifecycle decisions.
- Treat `references/` as detailed guidance, not independently selectable skills.
