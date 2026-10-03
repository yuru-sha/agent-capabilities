---
name: frontend-svelte
description: "Use when building or reviewing Svelte 5 components, runes, snippets, reactivity, or SvelteKit load and form behavior."
---

# Svelte 5

Use with `frontend-web-quality` and the repository's TypeScript specialists.
Preserve legacy Svelte code unless a scoped migration is requested.

## Rules

- Use Svelte 5 runes for new reactive code: `$state` for source state,
  `$derived` for pure computed state, `$props` for component inputs, and
  `$effect` only for external synchronization in the browser.
- Keep `$derived` expressions free of side effects. Avoid setting state inside
  `$effect`; return teardown functions for timers, subscriptions, observers,
  and other resources.
- Use current Svelte 5 event and composition APIs for new code, but do not
  rewrite legacy `on:` handlers or slots without a migration reason and a
  focused verification plan.
- In SvelteKit, keep private environment variables and database access in
  `+page.server` or other server-only modules. Use universal `load` only for
  data safe to run in both server and browser contexts, and use generated
  `$types` for route data contracts.
- Keep SSR, hydration, navigation, form submission, pending, error, and
  invalidation behavior explicit. Treat `{@html}` content and loaded data as
  untrusted and sanitize it at the appropriate boundary.
- Test rendered behavior rather than compiler details, including keyboard
  interaction, server/client data boundaries, hydration, and failed loads or
  actions where relevant.

## References

- [What are runes?](https://svelte.dev/docs/svelte/what-are-runes)
- [`$state`](https://svelte.dev/docs/svelte/$state)
- [`$derived`](https://svelte.dev/docs/svelte/$derived)
- [`$effect`](https://svelte.dev/docs/svelte/$effect)
- [SvelteKit loading data](https://svelte.dev/docs/kit/load)
