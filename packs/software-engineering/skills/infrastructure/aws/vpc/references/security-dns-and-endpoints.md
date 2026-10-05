# Security, DNS, and endpoints

Security groups are stateful workload firewalls; NACLs are stateless subnet controls. Prefer security groups for application trust relationships and use NACLs only when subnet-level policy adds real value.

Enable and verify VPC DNS support/hostnames when private service discovery or endpoint DNS depends on them.

For interface/gateway endpoints, review endpoint policy, route/DNS behavior, security groups, service support, and cost.

Do not assume a private subnet prevents data exfiltration when NAT, endpoints, or peered/transit routes still permit egress.
