---
name: infrastructure-reviewer
description: Select the matching provider-neutral Terraform specialist skills for infrastructure changes; route to the right specialists without owning the review lifecycle.
---

# Infrastructure specialist selector

Route Terraform infrastructure changes to the matching specialist contracts.
OMP's independent `reviewer` role owns the review session. oh-my-pstack's
`interrogate` is an explicit adversarial multi-model panel, invoked only when
the caller requests it.

## Select

1. Identify the Terraform change surface from the diff or spec.
2. Load only the matching specialist:
   - module/provider/state/plan/lifecycle concerns:
     `terraform-infrastructure`
   - policy-as-code, static checks, and infrastructure test concerns:
     `terraform-policy-testing`
3. Hand the specialist bundle to the OMP `reviewer` role. Invoke pstack
   `interrogate` only if the caller explicitly asks for adversarial or
   multi-model review.

Cloud-provider service knowledge is not owned by this selector. Install and use
the official provider Agent Skills directly:

- AWS: `aws/agent-toolkit-for-aws`
- Google Cloud: `google/skills`

Do not run Terraform apply or destroy, mutate cloud resources, alter remote
state, change GitHub state, or print secret values. Report each finding with
severity, location, scenario, evidence, and the smallest safe remediation.
