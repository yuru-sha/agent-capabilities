# Capacity, networking, and identity

Choose EC2 or Fargate capacity from workload requirements. With capacity providers, define base/weight and scaling ownership clearly.

For awsvpc networking, account for subnet IPs, ENIs, security groups, DNS, and load-balancer target type.

The execution role supports ECS/platform actions such as image pull/log delivery; the task role is the application workload identity. Do not merge them for convenience.

Keep secrets and configuration references explicit and least-privileged.
