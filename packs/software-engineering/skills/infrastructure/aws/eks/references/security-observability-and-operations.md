# Security, observability, and operations

Use least-privilege Kubernetes RBAC and AWS IAM independently. Review cluster-admin grants, access entries, service accounts, pod security controls, secrets handling, and admission policies.

Enable control-plane logs and collect workload/node signals needed for incident response. Monitor scheduling failures, node readiness, pod restarts, throttling, DNS/CNI issues, load balancer health, and autoscaler decisions.

Use immutable image references and scan/sign images according to the repository's supply-chain policy.

Back up and test restore procedures for cluster-scoped configuration and persistent application data separately.

Document break-glass access, node replacement, failed rollout recovery, and cluster upgrade rollback limits.
