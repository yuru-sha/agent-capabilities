---
name: step-functions
description: "Use when designing, implementing, reviewing, operating, or troubleshooting AWS Step Functions state machines, Standard or Express workflows, retries, catches, Map states, service integrations, callbacks, executions, or workflow reliability."
---

# step-functions

Use this skill for step-functions-specific AWS behavior. Compose it with adjacent service Skills when broader architecture is in scope.

## Reference routing

- workflow-types-and-state-design -> references/workflow-types-and-state-design.md
- integrations-retries-and-operations -> references/integrations-retries-and-operations.md

## Rules

- Choose Standard vs Express from duration, semantics, auditability, and cost.
- Keep retries and catches explicit per failure class.
- Treat service integrations as distributed side effects.
- Bound Map and parallel concurrency.
- Prefer visible workflow state over hidden orchestration logic.
- Treat references/ as detailed guidance, not independently selectable skills.
