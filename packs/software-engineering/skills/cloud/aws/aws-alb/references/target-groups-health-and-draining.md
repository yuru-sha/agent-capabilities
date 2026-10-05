# Target groups, health, and draining

Select target type and protocol/port from the workload networking model.

Health-check path, success codes, interval, timeout, thresholds, and grace periods should represent real readiness, not only process existence.

Coordinate deregistration delay with ECS/EKS/EC2 shutdown and connection draining.

Use slow start for workloads that pass readiness before caches/JIT/connections are fully warm.
