---
name: typescript-dom-accessibility
description: "Use when TypeScript changes browser DOM or UI behavior, forms, focus management, keyboard interaction, or accessibility semantics."
---

# TypeScript DOM and Accessibility

Use only when browser UI is in scope. Compose with the existing UI framework
and test tooling instead of introducing a new accessibility abstraction.

## Check

- Prefer semantic HTML and native controls; add ARIA only when the native element cannot express the behavior.
- Verify keyboard operation, visible focus, labels, names, roles, states, error associations, loading, and disabled behavior.
- Keep focus movement and live-region announcements deterministic across validation, dialogs, navigation, and async updates.
- Avoid unsafe DOM sinks and validate or escape untrusted content before insertion.
- Use the repository's accessibility checks plus a focused keyboard/screen-reader-oriented interaction test where feasible.

