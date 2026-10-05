# Scaling, cost, and operations

Scale from workload demand and downstream capacity, not only CPU. Queue depth, request concurrency, latency, and custom application metrics may be better signals.

Set hard minimum/maximum capacity and account for startup delay during scale-out.

Use Fargate Spot only when interruption can be tolerated. Handle termination signals, stop accepting new work, checkpoint or abandon safely, and keep retry/idempotency behavior correct.

Compare cost with EC2-backed capacity including utilization, Savings Plans/discounts, operational overhead, and idle headroom.

Monitor task/pod launch failures, insufficient IPs, image pull failures, OOM/CPU saturation, restart churn, and downstream throttling.
