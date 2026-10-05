# Metrics, alarms, and dashboards

Choose metrics from the workload's availability, latency, errors, saturation, backlog, and dependency-health requirements.

Use namespaces and dimensions consistently. Avoid dimensions with unbounded cardinality because they create excessive time series, cost, and operational noise.

For alarms, document:

- metric or metric math;
- statistic and period;
- threshold and comparison;
- datapoints/evaluation periods;
- missing-data behavior;
- severity and owner;
- runbook and notification target.

Use dashboards to support diagnosis, not as a substitute for alerts. Place correlated workload, dependency, deployment, and capacity signals together when that shortens incident triage.
