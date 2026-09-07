---
name: go-dependencies
description: "Use when Go code involves go.mod, go.sum, module selection, or dependency security."
---

# Go Dependencies

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Go-specific decisions for this concern.

## Rules

- Preserve go.mod and go.sum conventions; add a module only for a concrete capability not already available.
- Keep versions and provenance reviewable and run the repository's existing vulnerability and license checks.
- Do not turn dependency cleanup into an unrelated upgrade.

