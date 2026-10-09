---
name: typescript-resource-management
description: "Use when TypeScript or Node/browser code involves streams, timers, listeners, clients, workers, or disposal."
---

# TypeScript Resource management

Use this specialist with the project's TDD workflow for implementation and the project's review workflow for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Release clients, streams, timers, listeners, workers, and locks in finally or the repository's established disposal pattern.
- Define ownership and shutdown for AbortControllers, event listeners, async tasks, and browser resources.
- Test cancellation, rejection, and partial cleanup rather than only successful completion.

