# Availability and recovery

Define availability from the business requirement, not from the number of Availability Zones shown in a diagram.

For each critical path, identify:

- single-AZ and single-Region dependencies;
- stateful recovery requirements;
- RTO and RPO targets;
- health detection and failover trigger;
- failover and failback owner;
- degraded-mode behavior;
- data reconciliation after recovery.

Multi-AZ improves some failure modes but does not automatically provide disaster recovery. Multi-Region designs add replication, consistency, routing, deployment, and operational complexity that must be justified.

Test backup restore, replacement, failover, and rollback paths with service-specific procedures. A successfully provisioned standby is not evidence that the application can recover safely.
