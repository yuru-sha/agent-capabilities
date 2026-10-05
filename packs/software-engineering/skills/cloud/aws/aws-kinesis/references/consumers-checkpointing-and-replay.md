# Consumers, checkpointing, and replay

## Delivery semantics

Design consumers as at-least-once processors. A record can be processed again after worker failure, checkpoint lag, lease movement, replay, or downstream retry.

Make side effects idempotent using business keys, conditional writes, deduplication state, or transactional boundaries appropriate to the sink.

## KCL and leases

The Kinesis Client Library uses leases/checkpoints to coordinate shard ownership across workers and stores that coordination state in DynamoDB. Treat the lease table as operational state with its own IAM, capacity, lifecycle, and observability requirements.

Consumers must handle shard splits/merges and parent/child progression correctly; do not hard-code a fixed shard topology.

## Checkpointing

Checkpoint after the application's durable side effects for the covered records are complete. Checkpointing too early can lose processing; checkpointing too late increases duplicates during recovery.

Choose checkpoint frequency from replay cost, duplicate tolerance, latency, and downstream transaction boundaries.

## Enhanced Fan-Out

Use Enhanced Fan-Out when each registered consumer needs dedicated read throughput and low-latency push delivery. Prefer shared-throughput polling when consumer count, latency, and throughput do not justify EFO.

## Replay

Replays must be observable and bounded. Record the chosen starting point, expected volume, consumer concurrency, sink impact, and completion criteria before starting a large replay.
