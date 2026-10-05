# Tasks, services, and deployments

Define container image, command, CPU/memory, ports, health checks, environment, secrets, logging, volumes, and dependencies in the task definition.

Use services for long-running desired-count workloads and standalone tasks for bounded execution where appropriate.

For rolling deployments, define minimum/maximum healthy percentages, health-check grace, rollback/circuit-breaker behavior, and draining.

Promote immutable image digests or otherwise controlled image references so rollback identifies a known artifact.
