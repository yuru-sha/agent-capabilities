# Autoscaling, add-ons, and upgrades

Use HPA/VPA/KEDA for workload scaling where appropriate and Cluster Autoscaler or Karpenter for node capacity according to the repository's chosen ownership model.

Set explicit minimum/maximum bounds and understand scale-down disruption. Pair autoscaling with PodDisruptionBudgets, topology spread, requests/limits, and startup probes.

Treat core add-ons such as VPC CNI, CoreDNS, kube-proxy, CSI drivers, and AWS Load Balancer Controller as versioned dependencies.

Upgrade control plane, add-ons, nodes, and workloads in a tested order. Read deprecation and API-removal notes before version jumps.

Do not mix two node autoscalers without clearly partitioned responsibility.
