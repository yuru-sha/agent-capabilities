# SQS DLQ and recovery

A dead-letter queue is a failure isolation mechanism, not a complete recovery strategy.

- Create the DLQ explicitly and match queue type: Standard → Standard, FIFO → FIFO.
- Set `maxReceiveCount` from realistic transient-failure behavior; too low sends recoverable messages to the DLQ, too high delays detection of poison messages.
- Preserve enough message/context data to diagnose why processing failed.
- Monitor DLQ depth and oldest-message age.
- Define who owns triage, how a message is fixed, and how it is replayed/redriven.
- Ensure replay is idempotent.
- Validate retention periods so DLQ messages do not expire before investigation.
- Avoid endless source↔DLQ loops; redrive should happen after the underlying failure is understood or explicitly accepted.
