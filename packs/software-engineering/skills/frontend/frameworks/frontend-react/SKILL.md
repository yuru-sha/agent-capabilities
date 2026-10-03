---
name: frontend-react
description: "Use when building or reviewing React 19 components, Actions, form Hooks, transitions, Suspense, or React server/client boundaries."
---

# React 19

Use with `frontend-web-quality` and the repository's TypeScript specialists.
Keep React-specific guidance here; use the framework Skill for Next.js or
another React host.

## Rules

- Read the installed React and renderer versions before choosing an API. Keep
  components pure, derive values during render, and keep state to the smallest
  source of truth. Use stable keys for collections whose order or membership
  can change.
- For async form mutations, prefer React 19's documented Actions and form
  Hooks when the project supports them: `useActionState` for result and error
  state, `useFormStatus` for pending UI, and `useOptimistic` only when the
  operation can reconcile or roll back a failed update.
- Keep validation errors, pending state, disabled behavior, and retry paths
  visible and accessible. Do not hide server errors in console output or let an
  optimistic value become the permanent source of truth by accident.
- Use `useEffect` for synchronization with external systems such as DOM APIs,
  subscriptions, or third-party widgets. Derive React state directly when no
  external system is involved, and return cleanup for subscriptions, timers,
  and abortable work.
- Treat Server Components, Server Functions, `use`, and Suspense as host and
  build-tool capabilities. Keep browser-only APIs and event handlers in client
  modules and pass only serializable data across a server/client boundary.
- Test public behavior for pending, success, validation failure, thrown error,
  retry, optimistic failure, hydration, and keyboard interaction when relevant.

## References

- [React v19](https://react.dev/blog/2024/12/05/react-19)
- [`useActionState`](https://react.dev/reference/react/useActionState)
- [Built-in React DOM Hooks](https://react.dev/reference/react-dom/hooks)
- [`useOptimistic`](https://react.dev/reference/react/useOptimistic)
