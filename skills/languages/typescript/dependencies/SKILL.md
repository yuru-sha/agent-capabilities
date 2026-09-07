---
name: typescript-dependencies
description: "Use when TypeScript or Node/browser code involves package manifests, lockfiles, package managers, or dependency security."
---

# TypeScript Dependencies

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only TypeScript-specific decisions for this concern.

## Rules

- Preserve the repository's package manager and lockfile; add a package only for a concrete capability local code cannot safely provide.
- Review runtime and browser compatibility, provenance, install scripts, and license/security checks already used by the project.
- Do not mix dependency upgrades with an unrelated feature.

