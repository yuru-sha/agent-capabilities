# Performance, scaling, and operations

Choose instance/storage class, IOPS/throughput, and replica count from measured load.

Monitor connections, CPU, memory pressure, storage/IO latency, replica lag, deadlocks/locks via engine tooling, and failover events.

Use Performance Insights/Database Insights or engine-native observability as appropriate.

Coordinate application retry/backoff and connection recovery with failover behavior; do not assume existing connections survive endpoint failover cleanly.
