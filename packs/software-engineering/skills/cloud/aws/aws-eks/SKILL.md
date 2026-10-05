---
name: aws-eks
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon EKS clusters, node groups, Pod Identity/IRSA, networking, ingress, autoscaling, add-ons, upgrades, or Kubernetes workload security on AWS."
---

# aws-eks

Use this skill for EKS-specific Kubernetes control-plane and AWS integration concerns. Compose it with Kubernetes- or language-specific guidance when application behavior is also in scope.

## Reference routing

- `cluster-and-node-lifecycle` → `references/cluster-and-node-lifecycle.md`
- `identity-networking-and-ingress` → `references/identity-networking-and-ingress.md`
- `autoscaling-addons-and-upgrades` → `references/autoscaling-addons-and-upgrades.md`
- `security-observability-and-operations` → `references/security-observability-and-operations.md`

## Rules

- Separate control-plane, node, pod, and AWS service identities.
- Treat networking, CNI, subnet capacity, security groups, and ingress/load-balancer behavior as one design.
- Prefer workload identity through EKS Pod Identity or IRSA over node-role credential inheritance.
- Keep cluster/add-on/node-group versions aligned with an explicit upgrade plan.
- Define autoscaling limits, disruption budgets, and workload placement before relying on automatic scaling.
- Keep service-specific AWS behavior in the relevant service Skill; EKS owns Kubernetes-on-AWS integration and cluster lifecycle.
- Treat `references/` as detailed guidance, not independently selectable skills.
