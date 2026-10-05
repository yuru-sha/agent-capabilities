---
name: aws-lambda
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Lambda functions, invocation models, runtimes, concurrency, event source mappings, retries, destinations, versions/aliases, VPC configuration, or serverless reliability."
---

# aws-lambda

Use this skill for language-independent Lambda behavior. Compose it with the relevant language Skill for runtime-specific build, dependency, module, and packaging guidance.

## Reference routing

- `invocation-retries-and-idempotency` → `references/invocation-retries-and-idempotency.md`
- `concurrency-performance-and-lifecycle` → `references/concurrency-performance-and-lifecycle.md`
- `event-sources-networking-and-operations` → `references/event-sources-networking-and-operations.md`

## Rules

- Distinguish synchronous, asynchronous, and poll-based event-source invocation because their retry and failure semantics differ.
- Design handlers and downstream effects for duplicate delivery whenever the trigger can retry.
- Set timeout, memory, ephemeral storage, architecture, and concurrency from measured workload behavior rather than defaults.
- Use reserved/provisioned concurrency only with a clear isolation, capacity, or latency objective.
- Align event-source visibility/retention, batch behavior, partial failures, destinations/DLQs, and downstream limits.
- Treat versions and aliases as deployment/runtime contracts; use immutable revisions for controlled rollout and rollback.
- Use VPC attachment only when the function needs private-network resources and account for network dependencies and cold-path behavior.
- Keep runtime/language packaging rules in the corresponding language Skill.
- Treat `references/` as detailed guidance, not independently selectable skills.
