---
name: frontend-nextjs
description: "Use when building or reviewing Next.js applications, especially App Router routes, Server/Client Components, navigation, caching, revalidation, or loading and error boundaries."
---

# Next.js

Use with `frontend-web-quality` and `frontend-react`. Inspect the installed
Next.js version and the router in use before applying guidance.

## Rules

- Keep the existing Pages Router or App Router boundary unless migration is
  explicitly requested. Do not mix their conventions or import paths.
- In the App Router, keep layouts and pages as Server Components by default.
  Add Client Components only for state, event handlers, lifecycle logic, or
  browser APIs, and keep providers and client subtrees as deep and small as
  possible.
- Fetch data and access private server resources in server code. Pass the
  smallest serializable data needed by client components; keep credentials,
  private environment variables, and authorization checks on the server.
- Give each route's loading, empty, not-found, and error behavior an explicit
  UI boundary. Preserve accessible status, focus, retry, and navigation when
  using `loading`, `error`, `not-found`, Suspense, or streaming.
- Treat caching as an explicit contract. Follow the installed version's
  configured model (`use cache`/Cache Components or the previous model), define
  freshness and invalidation, and never cache user-specific data under a shared
  key. Use tag or path invalidation that matches the mutation's scope.
- Prefer framework navigation primitives for route transitions and preserve
  URL, back/forward, scroll, and prefetch behavior. Validate form and route
  inputs on the server and return field-level or form-level errors to the UI.
- Verify static versus dynamic rendering, RSC serialization, cache invalidation,
  route transitions, and production `next build` behavior in addition to the
  user-flow tests.

## References

- [Next.js App Router](https://nextjs.org/docs/app)
- [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Revalidating](https://nextjs.org/docs/app/getting-started/revalidating)
- [Production checklist](https://nextjs.org/docs/app/guides/production-checklist)
