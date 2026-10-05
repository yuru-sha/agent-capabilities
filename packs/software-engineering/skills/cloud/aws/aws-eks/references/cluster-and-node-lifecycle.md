# Cluster and node lifecycle

Define cluster version, endpoint access, control-plane logging, authentication mode, and managed add-ons explicitly.

For compute, distinguish managed node groups, self-managed nodes, and Fargate profiles by workload requirements, daemonset needs, instance control, startup behavior, and cost.

Pin AMI or release-channel expectations when reproducibility matters. Treat node replacement and draining as routine operations, not exceptional events.

Capacity planning must include pod density, ENI/IP availability, daemonset overhead, system pods, and disruption during rolling updates.

Document bootstrap, node labels/taints, architecture, and storage/network dependencies for every node group.
