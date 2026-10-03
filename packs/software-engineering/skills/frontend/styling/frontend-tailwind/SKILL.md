---
name: frontend-tailwind
description: "Use when building or reviewing Tailwind CSS v4 or later styling, theme tokens, responsive variants, utility composition, or v3-to-v4 migration."
---

# Tailwind CSS v4+

Use with `frontend-web-quality`. Inspect the installed Tailwind version and
existing CSS/configuration before changing the styling pipeline.

## Rules

- For v4, prefer the CSS-first entry point (`@import "tailwindcss"`) and
  `@theme` for design tokens. Treat theme variables as the shared design API;
  keep semantic colors, typography, spacing, and breakpoints centralized.
- Preserve existing v3 configuration during an incremental migration. Use
  legacy `@config` only as a deliberate bridge, and verify v4 changes because
  v4 does not support the v3 `corePlugins`, `safelist`, or `separator` options.
- Keep utility usage readable and content-driven. Avoid constructing class
  names from arbitrary runtime fragments; use complete variants or the
  documented source mechanism when a class must be retained.
- Use responsive and container-based variants from the content constraints,
  not a device catalogue. Prefer native CSS when it is clearer, and extract a
  component or shared pattern when the same utility group has repeated meaning.
- Styling does not provide semantics or accessibility by itself. Preserve
  source order, focus visibility, contrast, reduced-motion behavior, and form
  states in the markup and interaction logic.
- Check the browser matrix before adopting v4: the current upgrade guide lists
  Safari 16.4+, Chrome 111+, and Firefox 128+ as its baseline. Keep v3.4 or
  document a fallback when the product must support older browsers.
- Verify generated CSS, class discovery, dark or forced-color modes, responsive
  widths, focus states, and the production build after styling changes.

## References

- [Tailwind CSS v4](https://tailwindcss.com/blog/tailwindcss-v4)
- [Functions and directives](https://tailwindcss.com/docs/functions-and-directives)
- [Theme variables](https://tailwindcss.com/docs/theme)
- [Upgrade guide](https://tailwindcss.com/docs/upgrade-guide)
