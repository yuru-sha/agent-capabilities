# Fargate runtime

Choose Fargate when removing node management is worth its workload constraints and pricing model. Validate supported CPU/memory combinations, architecture, ephemeral storage, networking, and platform behavior rather than treating "serverless containers" as the only decision criterion.

Each Fargate task or pod consumes workload-level networking capacity. Account for subnet IPs, ENIs, security groups, DNS, NAT or VPC endpoints, image pulls, and downstream connectivity.

Size CPU and memory from measured workload behavior. Include image-pull/startup latency and autoscaling delay in latency-sensitive capacity planning.

Use Fargate Spot only for interruption-tolerant workloads. Handle termination cleanly, stop accepting work, and keep retries/idempotency correct.

Keep durable state outside ephemeral task/pod storage unless the workload explicitly accepts loss on replacement.
