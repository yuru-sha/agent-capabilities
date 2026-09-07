---
name: test-fixture-design
description: "Use when designing shared test data, synthetic fixtures, golden files, snapshots, database fixtures, or adversarial test cases."
---

# Test Fixture Design

Compose with `$tdd` and the language/database/API testing skill. Fixtures are
test inputs, not a second source of truth for the implementation.

## Rules

- Keep fixtures minimal, deterministic, synthetic, and scoped to the behavior under test; never embed real secrets or personal data.
- Make the expected result independently understandable and avoid fixtures that merely mirror production code paths.
- Include positive, negative, boundary, malformed, empty, duplicate, ordering, permission, timeout, and cleanup cases where the contract needs them.
- Prefer builders or small named fixtures over giant snapshots; update golden files only with an intentional contract review.
- Ensure isolation, cleanup, stable paths/timestamps/IDs, and clear ownership when fixtures are shared across packages.

