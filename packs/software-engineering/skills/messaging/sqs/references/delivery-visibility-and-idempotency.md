# SQS delivery, visibility, and idempotency

Receiving a message does not remove it. SQS hides it for the visibility timeout; the consumer must delete it after successful processing.

## Visibility timeout

- Set visibility longer than normal processing plus network/read timeout margin.
- Extend visibility for genuinely long-running work instead of setting an excessively large queue-wide default.
- If processing exceeds visibility, the message can become visible and be processed by another consumer.
- Deleting with the wrong/stale receipt handle or losing the delete acknowledgement can produce ambiguous outcomes.

## Idempotency

- Use a business operation key, not only the SQS message ID, when the producer itself can retry or regenerate equivalent work.
- Persist deduplication state where duplicate side effects would be harmful.
- Design external API/database updates so replay is safe.
- Do not claim exactly-once end-to-end processing solely because FIFO is used.
