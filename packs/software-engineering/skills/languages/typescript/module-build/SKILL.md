---
name: typescript-module-build
description: "Use when TypeScript modules, ESM/CJS interop, tsconfig, project references, declaration output, or bundler behavior are changing."
---

# TypeScript Module Build

Use with `typescript-package-publishing` for library packaging and with the
repository's actual runtime or bundler configuration.

## Check

- Align `module`, `moduleResolution`, package `type`, `exports`/`imports`, runtime, bundler, and test runner assumptions.
- Distinguish type-check-only, transpilation, bundling, declaration generation, and executable output; verify each required artifact.
- Check project references, incremental output, path aliases, source maps, and generated declarations from a clean build.
- Test both supported import forms or explicitly document the single supported form.
- Prefer the existing build toolchain; do not fix module ambiguity by adding ad hoc runtime loaders.

