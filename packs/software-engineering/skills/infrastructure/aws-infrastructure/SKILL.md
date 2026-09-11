---
name: aws-infrastructure
description: Use when designing or reviewing AWS infrastructure topology and service integration across VPC, ECS Fargate, Aurora, Redis, ALB, ECR, SQS, Lambda, S3, or Step Functions.
---

# AWS infrastructure

Trace the request, data, and failure paths across the AWS services in scope.
Use the consumer repository's regions, naming, deployment, and observability
conventions rather than inventing account-specific defaults.

## Rules

- Separate development, staging, and production accounts, regions, state, and
  credentials where the repository's boundary requires it. Make environment
  selection explicit and never use production resources as development
  defaults.
- Keep databases and caches in private subnets. Model VPC routes, endpoints or
  NAT, subnet placement, security-group references, DNS, and TLS together;
  avoid broad CIDR ingress when a workload or security-group reference is
  available.
- For ECS Fargate, distinguish the task role from the execution role, verify
  image provenance and pull access, and align ALB target ports, health checks,
  draining, timeouts, and deployment capacity with the service contract.
- For Aurora and Redis, review private connectivity, encryption, backups,
  failover or recovery behavior, parameter settings, connection limits, and
  security-group scope. Do not treat a healthy provisioning result as evidence
  that application retries or failover are safe.
- For ALB and ECR, check listener TLS, target health, immutable image
  references, image scanning, and rollback to a known artifact.
- For SQS, Lambda, S3, and Step Functions, check retry, timeout, idempotency,
  dead-letter or failure destinations, visibility timeout, concurrency,
  encryption, public-access blocking, and explicit error handling.
- Give each resource and field one owner. Keep long-lived infrastructure in
  Terraform or the consumer's chosen IaC boundary and keep application
  deployment concerns in the configured deployment tool.

## Verification

Inspect the configured Terraform plan or equivalent deployment diff,
configuration, IAM references, health checks, and operational alarms. Report
missing evidence separately from confirmed behavior; do not apply, destroy, or
make AWS changes as part of this specialist.
