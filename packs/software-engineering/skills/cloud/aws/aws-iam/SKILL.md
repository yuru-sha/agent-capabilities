---
name: aws-iam
description: "Use when designing or reviewing AWS IAM identities, policies, roles, trust policies, STS assumptions, iam:PassRole, permission boundaries, cross-account access, or AWS authorization failures."
---

# aws-iam

Use this skill for AWS identity and authorization. GitHub Actions workflow design and OIDC workflow integration stay in `github-actions-aws-deploy`; network security belongs to VPC/network Skills.

## Reference routing

- `policies-and-least-privilege` → `references/policies-and-least-privilege.md`
- `roles-trust-and-sts` → `references/roles-trust-and-sts.md`
- `passrole-boundaries-and-cross-account` → `references/passrole-boundaries-and-cross-account.md`

## Rules

- Grant the smallest required actions on the smallest resource set and add conditions when they materially reduce exposure.
- Review identity policies, resource policies, trust policies, session policies, permission boundaries, and organization controls as separate layers.
- Treat `iam:PassRole` as a privilege boundary and constrain both the role resource and the service that may receive it.
- Prefer short-lived STS credentials and workload roles over long-lived access keys.
- Separate deployment, execution, administration, and read-only identities where their authority differs.
- Validate authorization from the caller through every assumed role and resource-policy hop; a successful role assumption alone does not prove least privilege.
- Never expose credentials or secret values while debugging authorization.
- Treat `references/` as detailed guidance, not independently selectable skills.
