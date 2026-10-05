# Stream selection and event model

## Kinesis versus a queue

Choose Kinesis Data Streams when the workload needs one or more of:

- ordered processing within a partition key;
- multiple independent consumers reading the same event history;
- replay from retained data;
- high-throughput append-style event ingestion;
- stream-processing pipelines that track consumer position.

Choose SQS when the primary model is work distribution where a message should normally be completed by one consumer group and long-term replay is not the core contract.

Do not model a Kinesis stream as a FIFO queue with one global order. Ordering is scoped by partition-key/shard sequencing behavior, and parallelism comes from distributing records across keys/shards.

## Event contract

Define event type/version, producer identity, event time, entity/business key, idempotency key, and payload compatibility rules.

Prefer immutable events. When consumers need current state rather than an event history, consider whether a database/change stream or direct state lookup is a better source of truth.

## Retention and replay

Retention defines the replay window. Set it from recovery, reprocessing, downstream outage, and audit requirements rather than accepting the default implicitly.

Document how a new or recovered consumer selects its starting position and how duplicate side effects are prevented during replay.
