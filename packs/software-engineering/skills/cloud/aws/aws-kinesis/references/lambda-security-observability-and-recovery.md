# Lambda, security, observability, and recovery

## Lambda event source mappings

When Lambda consumes a stream, configure batch size, batching window, concurrency/parallelization, retry behavior, record age, bisect-on-error or partial batch response behavior according to the failure model.

Avoid retrying already-successful records when record-level failure reporting can isolate the bad subset. Make downstream writes idempotent because Lambda stream processing can redeliver records.

## IAM and encryption

Use least-privilege IAM for producers, consumers, enhanced fan-out registration/subscription, stream administration, and KCL lease tables. Treat KMS permissions as part of the data-path contract when customer-managed keys are used.

## Metrics

Monitor at least:

- write/read throttling;
- incoming records/bytes;
- consumer iterator age or equivalent lag;
- Lambda errors, throttles, duration, concurrency, and iterator age when Lambda is used;
- shard-level metrics when diagnosing skew/hot shards;
- KCL/DynamoDB lease-table health for KCL consumers.

## Recovery

Document consumer restart/redeployment behavior, checkpoint ownership, replay start position, retention window, duplicate handling, and downstream reconciliation.

Before shortening retention or deleting a stream, verify that no active or recovery consumer still depends on the unread history.
