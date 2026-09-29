---
name: infrastructure-reviewer
description: Select the matching Terraform or AWS infrastructure specialist skills for a change; route to the right specialists without owning the review lifecycle.
---

# Infrastructure specialist selector

Route an infrastructure change to the matching specialist contracts. OMP's
independent `reviewer` role owns the review session. oh-my-pstack's
`interrogate` is an explicit adversarial multi-model panel, invoked only when
the caller requests it. This selector only chooses specialist contracts.

## Select

1. Identify the change surface from the diff or spec.
2. Load only the matching specialist:
   - Terraform plans, state, providers, policy tests:
     `terraform-infrastructure` and `terraform-policy-testing`.
   - AWS topology and service failure paths: `aws-infrastructure`.
   - IAM, OIDC, secrets, network trust: `aws-iam-oidc-security`.
   - GitHub Actions, ECS, ecspresso handoffs: `github-actions-aws-deploy`.
   - Lambda runtime, dependencies, packaging: `nodejs-lambda`.
   - Metrics, alarms, Slack delivery, incident response:
     `cloudwatch-operations`.
3. Hand the specialist bundle to the OMP `reviewer` role. Invoke pstack
   `interrogate` only if the caller explicitly asks for adversarial or
   multi-model review.
   Do not run Terraform apply or destroy, deploy AWS resources, change IAM or
   network rules, alter GitHub state, or print secret values. Report each
   finding with severity, location, scenario, evidence, and the smallest safe
   remediation.