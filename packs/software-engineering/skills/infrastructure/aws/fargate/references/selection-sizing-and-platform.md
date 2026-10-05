# Selection, sizing, and platform

Compare Fargate with EC2-backed ECS/EKS when workloads need privileged access, host networking, specialized accelerators, daemonsets, custom AMIs, very high density, or predictable long-running capacity economics.

Validate allowed vCPU/memory combinations, CPU architecture, operating system, and platform version before deployment.

Size from measured CPU, memory, startup, and burst behavior. Avoid permanently over-sizing to compensate for unbounded concurrency or downstream bottlenecks.

For latency-sensitive workloads, include image pull, startup, ENI attachment, and autoscaling delay in the service objective.
