# SQS queue selection and message model

## Standard

Use Standard queues when very high throughput and horizontal consumption matter more than strict ordering. Delivery is at least once, so consumers must tolerate duplicates.

## FIFO

Use FIFO when ordering and deduplication semantics are required.

- Queue names end in `.fifo`.
- `MessageGroupId` defines the ordering/concurrency boundary.
- Messages in one group are processed in order; a blocked/in-flight message can hold later messages in the same group.
- `MessageDeduplicationId` or content-based deduplication helps suppress duplicate sends within the service's deduplication window, but application side effects should still be idempotent.

## Payloads

- Keep messages small and versioned.
- Current SQS message size limits must be verified against AWS docs; use object storage plus references for oversized payloads rather than embedding large binaries.
- Do not place sensitive information in queue names.
- Include correlation, schema version, operation ID/idempotency key, and tracing metadata where useful.
