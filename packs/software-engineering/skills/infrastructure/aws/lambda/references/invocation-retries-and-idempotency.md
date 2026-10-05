# Invocation, retries, and idempotency

## Synchronous invocation

The caller receives the function result or error and owns request-level retry decisions. Bound caller retries and make mutations safe against duplicate attempts.

## Asynchronous invocation

Lambda queues the event and applies asynchronous retry/failure-destination behavior. Configure event age, retries, destination or DLQ, and operator recovery intentionally.

## Poll-based event sources

For SQS, Kinesis, DynamoDB Streams, and similar mappings, reason from the source's delivery, visibility/retention, ordering, batch, and checkpoint semantics.

Use partial batch failure where supported when successful records should not be replayed with failed records.

## Idempotency

Do not claim exactly-once execution. Use business identifiers, conditional writes, deduplication records, or transactional sink behavior when duplicate side effects matter.
