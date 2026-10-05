---
name: cloudwatch
description: "Use when designing, implementing, reviewing, operating, or troubleshooting Amazon CloudWatch metrics, logs, alarms, dashboards, Logs Insights queries, retention, anomaly detection, or alerting for AWS workloads."
---

# Amazon CloudWatch

Use this skill for CloudWatch-specific observability and operations. Service-specific metrics remain owned by the service Skill; CloudWatch owns collection, querying, alarming, dashboards, retention, and alert routing.

## Reference routing

- `metrics-alarms-and-dashboards` → `references/metrics-alarms-and-dashboards.md`
- `logs-and-insights` → `references/logs-and-insights.md`
- `alerting-retention-and-cost` → `references/alerting-retention-and-cost.md`

## Rules

- Start from user-visible failure and saturation signals, then select metrics and logs that detect them.
- Keep metric dimensions stable and bounded; avoid high-cardinality dimensions derived from request/user/error values.
- For every alarm, define statistic, threshold, evaluation period, missing-data behavior, severity, owner, runbook, and notification path.
- Prefer actionable composite or grouped alerting over one alarm per low-level symptom.
- Define log structure, retention, redaction, query fields, and investigation workflows explicitly.
- Monitor the monitoring path, including missing metrics, log delivery failures, and notification failures.
- Treat retention and custom-metric/log ingestion as cost-bearing design choices.
- Treat `references/` as detailed guidance, not independently selectable skills.
