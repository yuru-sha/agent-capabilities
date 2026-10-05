# SQS security, observability, and integrations

## Security

- Grant producers and consumers the minimum SQS actions they need.
- Use queue policies for cross-account/service access intentionally.
- SQS uses server-side encryption by default for new queues; use customer-managed KMS keys when policy or access boundaries require them.
- Include required KMS permissions when using customer-managed keys.
- Keep queue URLs/ARNs and credentials/configuration out of hard-coded application secrets.

## Observability

Track:
- visible, not-visible/in-flight, delayed messages;
- oldest message age;
- send/receive/delete rates;
- empty receives;
- DLQ depth and age;
- consumer error/retry/throttle rates.

## Integrations

- SNS → SQS: validate subscription permissions and message-envelope/raw-delivery expectations.
- EventBridge → SQS: validate target policy and event contract.
- Lambda ← SQS: configure batching, concurrency, visibility, partial failures, and DLQ/redrive coherently.
- ECS/EKS/EC2 workers: own polling loop, scaling, graceful shutdown, credential refresh, and delete semantics explicitly.
