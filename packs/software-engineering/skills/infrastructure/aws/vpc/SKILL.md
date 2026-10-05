---
name: vpc
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon VPC networks, subnets, route tables, NAT/Internet gateways, VPC endpoints, security groups, NACLs, DNS, or hybrid connectivity."
---

# Amazon VPC

Use this skill for AWS network topology and connectivity. Keep workload-specific behavior in the relevant compute or service Skill.

## Reference routing

- `topology-routing-and-egress` → `references/topology-routing-and-egress.md`
- `security-dns-and-endpoints` → `references/security-dns-and-endpoints.md`
- `capacity-connectivity-and-operations` → `references/capacity-connectivity-and-operations.md`

## Rules

- Design CIDR, subnet, AZ, route, DNS, and egress behavior together.
- Separate public, private application, and data-plane exposure intentionally.
- Prefer security-group references over broad CIDRs when workloads are known.
- Treat NAT gateways and public IPv4 as availability and cost decisions, not defaults.
- Use VPC endpoints when they materially reduce public egress or strengthen service access boundaries.
- Track subnet IP/ENI capacity for ECS, EKS, Lambda, load balancers, and other ENI-heavy services.
- Treat `references/` as detailed guidance, not independently selectable skills.
