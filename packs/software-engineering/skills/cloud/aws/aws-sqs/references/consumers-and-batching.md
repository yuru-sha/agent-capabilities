# SQS consumers and batching

- Prefer long polling to reduce empty responses and API cost.
- Ensure HTTP/request timeout exceeds `WaitTimeSeconds`.
- Batch send, receive, delete, and visibility changes where useful, while handling per-entry partial failures.
- Bound consumer concurrency from downstream capacity, not only queue backlog.
- Track in-flight message limits and account for them when scaling Standard queue consumers.
- Stop polling before shutdown, finish or abandon in-flight work deliberately, and avoid deleting unprocessed messages.

## Lambda

For SQS event source mappings:

- function timeout must fit within queue visibility timeout constraints;
- a failed batch normally causes successfully processed records to become visible again;
- enable `ReportBatchItemFailures` / partial batch responses when only failed records should be retried;
- for FIFO, preserve ordering when reporting failures and avoid processing later records in a group after an earlier failure when that would violate business order.

Test batches with one failing record, poison messages, timeouts, throttling, and downstream outages.
