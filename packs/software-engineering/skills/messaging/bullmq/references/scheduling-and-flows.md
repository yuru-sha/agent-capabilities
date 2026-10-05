# BullMQ scheduling and flows

## Delayed and scheduled work

- Use current BullMQ Job Scheduler APIs for recurring schedules; verify the installed BullMQ version before using older repeatable-job examples.
- Keep schedule identity deterministic so deployment does not accidentally create duplicates.
- Store timezone and business-calendar assumptions explicitly.
- Do not use a delayed job as a durable replacement for a business state machine when cancellation, rescheduling, or auditing is central.

## Flows

- Use `FlowProducer` when parent/child dependencies are part of one logical workflow.
- Keep flow depth and fan-out bounded.
- Define what happens when a child fails, retries, or is removed.
- Do not use flows to hide unrelated service orchestration; keep cross-domain ownership explicit.

## Priorities and rate limiting

- Verify how priorities interact with retries and waiting jobs.
- BullMQ rate limiting is global for a queue/worker configuration; compute effective behavior across the worker fleet.
- Avoid old examples relying on removed group-key rate-limit behavior.
