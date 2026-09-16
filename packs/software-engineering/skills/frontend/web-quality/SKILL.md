---
name: frontend-web-quality
description: "Use when building or reviewing framework-agnostic, user-facing web UI involving semantic HTML, responsive layout, browser compatibility, client-side state, loading UX, or Core Web Vitals."
---

# Frontend Web Quality

Use this specialist with the global `$tdd` skill for implementation and
`$code-review` for review. It owns cross-framework web UI decisions; compose
`frontend-react`, `frontend-nextjs`, `frontend-svelte`, or `frontend-tailwind`
when those technologies are in scope. Use language specialists for syntax and
framework specialists for framework mechanics.

## Inspect first

- Identify the rendering mode, route and data boundaries, supported browsers and
  input modalities, existing UI primitives, and the real user flow. Reuse the
  repository's patterns before adding a library or abstraction.
- Define the relevant states explicitly: initial, loading, success, empty,
  error, offline, disabled, and stale. Keep one source of truth, derive the
  view from it, and cancel or ignore stale asynchronous results.
- Keep navigable or shareable state in the URL and preserve back/forward
  behavior. Choose client rendering, server rendering, static generation, or
  streaming from the product and data constraints, then verify the choice.

## Design principles

- Keep server and client boundaries explicit. When the selected framework
  supports server rendering or Server Components, fetch data and render
  non-interactive UI on the server, then pass only the smallest serializable
  props to client code. Keep event handlers, browser APIs, and client state in
  client modules; never cross the boundary with secrets.
- Minimize initial delivery: shipped JavaScript, serialized data, render-blocking
  work, and client-side abstractions. Prefer a simple rendering path over
  speculative architecture, then prove the result with measurements.
- Make code AI-readable: keep types explicit at network, form, and component
  boundaries; name state transitions; keep modules cohesive; and leave a
  focused verification path. AI assistance does not replace review, type
  checks, security validation, or behavior tests.

## Platform-first UI

- Use semantic HTML and native controls before custom elements. Use CSS for
  layout and styling, feature detection for capability checks, and Baseline for
  browser-support decisions; use user-agent detection only for a verified bug.
- Add ARIA only when native semantics cannot express the widget, and implement
  the corresponding accessible name, role, state, focus, and keyboard behavior.
  Treat WCAG 2.2 AA as the default target where applicable.
- Make layouts content-driven and resilient to narrow viewports, zoom, text
  resizing, touch, keyboard input, and right-to-left content. Preserve logical
  source and focus order, visible focus, sufficient target size, and a
  `prefers-reduced-motion` path.
- Treat network, URL, storage, and rendered HTML data as untrusted. Use safe
  DOM/rendering sinks, allowlist navigations where needed, and keep secrets out
  of client bundles. Compose the TypeScript security or repository security
  review specialist for detailed threat analysis.

## Delivery and performance

- Keep critical content useful in the initial response and progressively enhance
  optional behavior when the rendering mode permits. Reserve media dimensions,
  serve responsive images, defer below-the-fold work, and code-split
  non-critical routes or features.
- Measure before optimizing with the repository's tools and a representative
  workload. Check field and lab data separately; use the current Core Web
  Vitals targets at the 75th percentile for mobile and desktop: LCP <= 2.5s,
  INP <= 200ms, and CLS <= 0.1. Record the measurement and workload behind a
  performance claim.
- Prefer the smallest client-side state and JavaScript that satisfies the
  interaction. Avoid speculative memoization, global state, or a UI library
  when existing platform and repository primitives cover the behavior.

## Verify

- Test user-visible behavior at public seams: keyboard-only operation, focus
  visibility and restoration, labels and errors, loading/empty/error states,
  responsive layouts, text resize or zoom, reduced motion, and slow or failed
  network paths when relevant.
- Run the repository's existing accessibility, type, lint, build, and browser
  checks. Use targeted interaction tests for behavior and visual checks for
  layout; snapshots alone do not prove accessibility or responsiveness.
- Check every newly used web feature against the supported browser matrix and
  provide a fallback or a documented support boundary when it is not Baseline.

## References

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [MDN Baseline compatibility](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
- [Web Vitals](https://web.dev/articles/vitals)
- [Learn Performance](https://web.dev/learn/performance/)
