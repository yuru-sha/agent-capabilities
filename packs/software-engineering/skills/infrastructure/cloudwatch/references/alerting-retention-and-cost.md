# Alerting, retention, and cost

Route alerts through the repository or organization's approved notification path. Do not embed webhook tokens or other secret values in alarm definitions or examples.

Group and deduplicate alerts so one dependency outage does not trigger an uncontrolled alarm storm. Use escalation levels that distinguish paging conditions from diagnostic warnings.

Treat custom metrics, high-resolution metrics, log ingestion, retention, dashboards, and query volume as cost drivers.

Periodically verify that alarms still have owners/runbooks and that obsolete log groups, dashboards, and metric streams are removed when their workloads disappear.
