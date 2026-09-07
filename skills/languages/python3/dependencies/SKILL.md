---
name: python3-dependencies
description: "Use when Python 3 code involves pyproject.toml, lockfiles, environments, or package security."
---

# Python 3 Dependencies

Use this specialist with the global `$tdd` skill for implementation and `$code-review` for review. It owns only Python 3-specific decisions for this concern.

## Rules

- Preserve pyproject.toml, the lockfile, and the repository's environment manager; add a package only for a concrete need.
- Review supported Python versions, install hooks, provenance, license, and vulnerability checks already configured.
- Do not combine an unrelated dependency upgrade with a feature.

