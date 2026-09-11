---
name: cloudwatch-operations
description: Use when designing or reviewing CloudWatch metrics, alarms, Environment dimensions, Slack notifications, dashboards, monitoring, or incident response for AWS workloads.
---

# CloudWatch operations

Design observability around actionable failure paths, not a list of enabled
services. Use the repository's configured notification and incident system.

## Rules

- Define the signals and owner for each workload: availability, latency,
  errors, saturation, queue age/depth, task health, database or cache health,
  Lambda failures, and Step Functions execution failures as applicable.
- Use a consistent Environment dimension with values selected by the
  consumer repository. Keep dimensions stable and bounded; avoid dimensions
  that create an alarm or metric series per request, user, or exception value.
- For each alarm, specify metric/statistic, threshold, evaluation period,
  missing-data behavior, severity, owner, runbook, and notification action.
  Pair deployment or dependency alarms with a usable dashboard and enough
  log context to investigate.
- Route alerts through the repository's approved SNS-to-Slack or equivalent
  integration without embedding webhook tokens or secret values. Deduplicate
  and group alerts so a single outage does not create an alert storm.
- Cover failure paths: ALB health and latency, ECS task churn, Aurora or Redis
  saturation and failover, SQS age and dead letters, Lambda errors/throttles
  and destinations, S3 access failures, and Step Functions retries or failed
  executions when those services are in scope.
- Include detection, triage, mitigation or rollback, escalation, and
  post-incident evidence. Monitor the monitoring path itself, including
  missing metrics and notification delivery failures.

## Verification

Inspect metric and alarm definitions, Environment values, notification
targets, dashboards, log retention and redaction, runbooks, and alert
delivery evidence. Do not assume an alarm is useful because it was created,
and do not change monitoring or notification state as part of this specialist.
