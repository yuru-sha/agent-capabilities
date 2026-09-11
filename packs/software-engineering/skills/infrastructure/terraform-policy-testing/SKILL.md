---
name: terraform-policy-testing
description: Use when designing or reviewing Terraform structural tests, dependency checks, security scanning, policy gates, or infrastructure regression prevention.
---

# Terraform policy testing

Use layered, repository-configured checks that fail on unsafe infrastructure
changes before deployment. Do not turn one scanner's output into a universal
policy without understanding the resource and environment.

## Rules

- Keep structural checks separate from policy checks: use the configured
  Terraform validation or test framework for types, references, module
  behavior, and expected outputs, then use policy or security checks for
  exposure, encryption, IAM, network, and tagging rules.
- Test dependency constraints and lockfile changes explicitly. Detect
  provider or module drift, unreviewed source changes, and incompatible
  version upgrades using the repository's configured toolchain.
- Check high-impact invariants such as isolated production state, encrypted
  data, blocked unintended public access, narrow IAM and security groups,
  required Environment or ownership metadata, and safe queue or Lambda
  failure handling.
- Add regression coverage for changed modules and affected environment
  compositions. Prefer small structural fixtures or plan-derived assertions
  that do not require an AWS account, real credentials, or secret values.
- Run configured scanners such as TFLint, tfsec, Trivy, Checkov, or an
  equivalent only when the repository already uses them or explicitly selects
  them. Record versions and justified exceptions; do not suppress findings
  globally to make a build green.
- Treat state, plan JSON, provider caches, and scan output as potentially
  sensitive. Redact or discard them according to repository policy, and keep
  apply, destroy, and live-account mutation outside the test gate.

## Verification

Run the consumer repository's structural tests, dependency checks, policy
scans, and regression suite. Confirm that the checks exercise the changed
module and environment path, not only an unrelated fixture, and report
unrun or account-dependent checks explicitly.
