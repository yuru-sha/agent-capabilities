---
name: terraform-infrastructure
description: Use when designing or reviewing Terraform modules, environment separation, state, variables and outputs, provider constraints, dependency locks, or Terraform validation workflows.
---

# Terraform infrastructure

Use this specialist for Terraform structure and lifecycle boundaries. Use
terraform-policy-testing for policy, security scanning, and regression-test
design.

## Rules

- Read the repository's Terraform version, backend, provider constraints,
  module layout, environment convention, wrappers, and CI commands before
  proposing changes.
- Keep modules cohesive and expose a small typed input/output contract. Avoid
  hidden provider configuration, environment-specific defaults, account IDs,
  fixed resource names, and secrets in source or variable defaults.
- Keep development and production in separate state and explicitly selected
  accounts, regions, and variable sets. Do not copy development state or
  silently widen production access.
- Treat state and plan files as sensitive operational data. Preserve remote
  state locking, encryption, versioning, recovery, and least-privilege
  backend access; never commit state, plans, credentials, or secret-bearing
  plan output.
- Declare provider requirements and commit the repository's dependency lock
  file. Use the configured Terraform and provider versions; do not hand-edit
  .terraform.lock.hcl or upgrade providers as unrelated cleanup.
- Give variables types, descriptions, and deliberate defaults. Mark sensitive
  values sensitive, pass secrets through the consumer's secret mechanism, and
  output only values consumers actually need.

## Verification

Use the consumer repository's wrappers and versions. At minimum, run the
configured equivalents of terraform fmt -check -diff, terraform validate, and
tflint; use a plan only with an approved, correctly isolated backend and
credentials. A plan is evidence to inspect, not authorization to apply or
destroy.
