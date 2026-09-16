---
name: frontend-browser-testing
description: "Use when verifying public, user-facing web flows in real browsers across engines, viewports, input modalities, SSR or hydration, navigation, loading or failure paths, or visual interaction behavior."
---

# Frontend Browser Testing

Use with `frontend-web-quality` and the global `$tdd` skill. Add a framework
specialist only when the application uses that framework. Reuse the project's
existing browser runner, fixtures, and test environment; this Skill does not
require a new browser-testing dependency.

## Scope

- Start from one public user flow and its observable outcome. Identify the
  rendering mode, routes, data boundaries, supported browser engines,
  viewports, input modalities, and existing runner before writing a test.
- Test through the rendered UI and public navigation surface. Prefer semantic
  locators and user-visible state over component internals, implementation
  selectors, or mocked framework behavior.

## Rules

- Cover the supported browser matrix and representative narrow, wide, zoomed,
  touch, pointer, and keyboard contexts when the product supports them. Keep a
  happy-path-only desktop test from standing in for responsive or modality
  coverage.
- For SSR and hydration, assert useful server-rendered content before
  JavaScript runs, then verify that hydration preserves it and enables the
  intended interaction without console or markup errors.
- Verify navigation, deep links, query state, back/forward behavior, focus
  movement, and scroll behavior when the flow changes the URL or route.
- Exercise loading, empty, slow, offline, server-error, and retry paths where
  they are part of the flow. Wait for observable conditions, not arbitrary
  delays, and keep network failures controlled and reproducible.
- Check visual interaction behavior such as visibility, overflow, layout
  usability, focus indication, and reduced-motion behavior. Use screenshot
  comparisons only when the repository already has a configured baseline and
  reviewable threshold.
- Isolate browser state and clean up created data. Do not turn a live external
  service or a single machine's rendering into an unexplained pass condition.

## Verify

Run the repository's existing browser, type, lint, build, and accessibility
checks that cover the changed flow. Record the command, browser engines,
viewport sizes, input modalities, and failure paths actually exercised.

## References

- [WebDriver](https://www.w3.org/TR/webdriver2/)
- [Web Platform Tests](https://web-platform-tests.org/)
