---
name: package-release-compatibility
description: "Use when releasing a library, CLI, service artifact, generated client, or package whose API, ABI, wire format, or install behavior must remain compatible."
---

# Package and Release Compatibility

Compose with the language-specific API/packaging skill and OpenAPI or database
migration skills where those contracts are included in the release.

## Check

- Identify source API, binary ABI, wire/schema, CLI, config, data, and operational compatibility surfaces separately.
- Verify versioning, deprecation, changelog, generated artifacts, package contents, reproducibility, provenance, and rollback behavior.
- Install or deploy the built artifact in a clean consumer environment and exercise supported entry points, migrations, and upgrade paths.
- Test mixed-version clients/servers or rolling deployment behavior when compatibility must span a transition.
- Preserve exact artifact and toolchain evidence; a successful local build is not release proof.

