# Scaling, observability, and recovery

Scale services from workload demand and downstream limits, using CPU/memory or application/backlog metrics as appropriate.

Monitor desired/running/pending tasks, deployment state, task exits, health failures, throttling, image pull failures, ENI/IP capacity, and downstream saturation.

Define recovery for failed deployments, stuck draining, dependency outage, and capacity shortages.

Avoid restart loops that amplify downstream incidents; use bounded retry/backoff at the application layer.
