---
name: python3-dependencies
description: "Use when Python 3 code involves pyproject.toml, lockfiles, environments, or package security."
---

# Python 3 Dependencies

Use oh-my-pstack's TDD workflow for implementation and its review workflow for review. This specialist owns only Python 3-specific decisions for this concern.

## Rules

- Preserve pyproject.toml, the lockfile, and the repository's environment manager; add a package only for a concrete need.
- Review supported Python versions, install hooks, provenance, license, and vulnerability checks already configured.
- Do not combine an unrelated dependency upgrade with a feature.

