# Identity, networking, and ingress

Use EKS Pod Identity or IRSA for pod-level AWS access where possible. Review trust policy, service account or association mapping, and role permissions together.

Treat VPC CNI behavior, subnet IP capacity, prefix delegation, security groups, DNS, and egress/NAT or VPC endpoints as a single networking contract.

For ingress, distinguish Kubernetes ingress/service semantics from the AWS Load Balancer Controller and ALB/NLB behavior. Define TLS termination, target type, health checks, source ranges, and security-group ownership.

Do not rely on the node IAM role as the default credential source for application pods.

Private clusters still need an explicit administrative and image/package egress path.
