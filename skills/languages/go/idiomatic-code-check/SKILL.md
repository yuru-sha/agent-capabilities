---
name: go-idiomatic-code-check
description: "Use when checking whether Go code follows repository and standard Go idioms, naming, error, context, interface, and package conventions."
---

# Go idiomatic-code check

Use this specialist with the global `$tdd` skill for implementation work and `$code-review` for review work. It owns only this language-specific concern.

## Rules

- Run the repository's gofmt, go vet, lint, and test commands when available; treat tool output as evidence, not the whole review.
- Check clear names, small cohesive packages, explicit errors, context propagation, correct defer placement, and interfaces introduced for real seams.
- Look for accidental range-variable/address capture, ignored errors, premature goroutines, needless pointer/interface use, and exported API drift.
- Prefer the smallest idiomatic change that matches neighboring Go code; do not impose a different style without a repository rule.

