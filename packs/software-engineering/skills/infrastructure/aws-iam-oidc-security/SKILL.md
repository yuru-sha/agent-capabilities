---
name: aws-iam-oidc-security
description: Use when reviewing AWS IAM least privilege, GitHub Actions OIDC trust, iam:PassRole, Secrets Manager access, or security-group boundaries.
---

# AWS IAM, OIDC, and network security

Review identity and network trust paths separately, then verify how they
compose. Keep all account, repository, environment, and secret values generic.

## Rules

- Grant the smallest required actions on the smallest resource set, with
  conditions for environment, tags, source, or encryption context where they
  materially reduce exposure. Separate deployment, execution, and read-only
  roles.
- Scope GitHub OIDC trust by the configured issuer, audience, repository, ref,
  and protected environment claims. Prefer short-lived role sessions and
  remove long-lived cloud credentials from repository secrets.
- Treat iam:PassRole as a privilege boundary: constrain both the role
  resource and the service that may receive it. Review the caller policy,
  trust policy, and target workload role together.
- Retrieve application secrets through the configured Secrets Manager path at
  runtime or through an approved injection mechanism. Do not place secret
  values in Terraform variables, plans, logs, artifacts, examples, or
  workflow output; review KMS and rotation access separately.
- Use security-group references and narrow ports between known workloads.
  Public ingress should be an explicit, justified edge-service boundary, not
  a default for administration, databases, caches, or internal queues.
- Check default-deny behavior, cross-account trust, resource policies, and
  failure paths. A valid Terraform plan or successful role assumption does not
  prove least privilege.

## Verification

Inspect rendered trust and identity policies, conditions, role attachment
paths, security-group rules, secret references, and the configured static
security checks. Redact secret values and stop at read-only evidence; never
change IAM, credentials, or network rules as part of this specialist.
