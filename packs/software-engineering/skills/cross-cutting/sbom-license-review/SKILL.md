---
name: sbom-license-review
description: "Use when dependency changes, release artifacts, SBOM generation, license policy, provenance, or transitive vulnerability evidence must be reviewed."
---

# SBOM and License Review

Compose with the repository's dependency, security, and release skills. Keep
tool output separate from the semantic review.

## Check

- Inspect direct and transitive dependencies, lockfiles, generated/vendor content, runtime images, and platform-specific artifacts.
- Generate or verify an SBOM in the repository's supported format and reconcile it with the actual shipped artifact.
- Check license policy, notices, dual-license choices, source obligations, provenance/signatures, and policy exceptions.
- Review vulnerability findings with affected code paths, reachability, fixed versions, and false-positive evidence; do not claim “clean” from an incomplete scan.
- Record tool versions, input revision, exclusions, and unresolved findings so the result is reproducible.

