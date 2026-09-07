---
name: python3-packaging
description: "Use when Python 3 packaging, pyproject metadata, wheels, sdists, entry points, editable installs, or supported versions change."
---

# Python 3 Packaging

Use with `package-release-compatibility` and the repository's chosen build and
environment tools.

## Check

- Keep project metadata, build backend, package discovery, dependencies, optional extras, entry points, and Python version constraints coherent.
- Build both required artifacts and inspect their contents; do not assume an editable install matches a wheel.
- Verify clean-environment installation, imports, console scripts, resource files, and compiled-extension behavior if applicable.
- Keep lockfiles, constraints, hashes, and reproducibility aligned with the supported workflow.
- Do not publish local paths, tests, credentials, caches, or generated files unintentionally.

