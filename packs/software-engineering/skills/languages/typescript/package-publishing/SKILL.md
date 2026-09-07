---
name: typescript-package-publishing
description: "Use when publishing or reviewing a TypeScript or JavaScript package, package exports, declaration files, or release artifacts."
---

# TypeScript Package Publishing

Use with `typescript-module-build`, `package-release-compatibility`, and the
repository's package-manager skill.

## Check

- Verify `exports`, `types`, `main`/`module`, `files`, `bin`, `typesVersions`, and ESM/CJS behavior against actual consumers.
- Separate runtime dependencies, peer dependencies, optional dependencies, and development-only packages correctly.
- Inspect the packed artifact, declarations, source maps, license files, and absence of source or secret files that should not ship.
- Run an install-and-import smoke test from a clean temporary consumer using the supported Node versions.
- Keep versioning, changelog, provenance, and rollback expectations consistent with the public API surface.

