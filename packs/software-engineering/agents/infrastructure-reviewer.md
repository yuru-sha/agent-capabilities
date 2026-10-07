---
name: infrastructure-reviewer
description: Route Terraform infrastructure changes to the matching official HashiCorp Agent Skills without owning the review lifecycle.
---

# Infrastructure specialist selector

Route Terraform infrastructure changes to the matching specialist contracts.
OMP's independent `reviewer` role owns the review session. pstack-omp's
`interrogate` is an explicit adversarial multi-model panel, invoked only when
the caller requests it.

## Select

1. Identify the Terraform change surface from the diff or spec.
2. Load only the matching official HashiCorp Terraform Skills. Typical routing:
   - style, modules, configuration, and refactoring: `terraform-style-guide` or
     `refactor-module`
   - Terraform tests: `terraform-test`
   - policy-as-code: `terraform-policy`
   - provider implementation: the matching `provider-*` Skill
   - import/discovery or Stacks: `terraform-search-import` or
     `terraform-stacks`
3. Hand the selected HashiCorp Skill bundle to the OMP `reviewer` role. Invoke pstack
   `interrogate` only if the caller explicitly asks for adversarial or
   multi-model review.

Cloud-provider service knowledge is not owned by this selector. Install and use
the official provider Agent Skills directly:

- AWS: `aws/agent-toolkit-for-aws`
- Google Cloud: `google/skills`
- Azure: `MicrosoftDocs/agent-skills`

Do not run Terraform apply or destroy, mutate cloud resources, alter remote
state, change GitHub state, or print secret values. Report each finding with
severity, location, scenario, evidence, and the smallest safe remediation.
