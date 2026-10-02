---
name: verify-agent-capabilities
description: Verify the agent-capabilities repository's Profile installer CLI with a disposable project; use when changing installer behavior, Profile resolution, or capability distribution metadata.
---

# Verify agent-capabilities

This repository distributes Skills, Agent selectors, Profiles, and Orca Automation prompts. It has no long-running application. The primary executable user path is `scripts/install-profile`; the other capabilities are metadata and instructions consumed by agent hosts. The recipes below run the actual installer against a disposable project and intercept only its external `gh skill install` boundary with a recording executable.

## Launch

From the repository root, create a unique scratch root and recording `gh` shim:

```sh
VERIFY_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/verify-agent-capabilities.XXXXXX")"
mkdir -p "$VERIFY_ROOT/bin" "$VERIFY_ROOT/project" "$VERIFY_ROOT/evidence"
cat > "$VERIFY_ROOT/bin/gh" <<'SH'
#!/bin/sh
printf '%s\n' "$*" >> "$VERIFY_GH_LOG"
exit 0
SH
chmod +x "$VERIFY_ROOT/bin/gh"
export VERIFY_ROOT VERIFY_GH_LOG="$VERIFY_ROOT/gh.log"
```

There is no server process to keep alive. Each drive runs the CLI directly. Readiness means the CLI exits and its expected output and shim log exist. Use a new `VERIFY_ROOT` for every run. Never point this recipe at a user project or share one root between concurrent runs.

## Doctor

From the repository root, run this read-only check before driving whenever checkout or scratch state looks wrong:

```sh
python3 -c 'from pathlib import Path; import sys; root=Path.cwd(); checks={"installer":(root/"scripts/install-profile").is_file(),"github_profile":(root/"profiles/github.yaml").is_file()}; print("root="+str(root), *[name+"="+str(ok) for name,ok in checks.items()]); sys.exit(0 if all(checks.values()) else 1)'
```

For an existing run, also confirm `VERIFY_ROOT/project` is a directory, `VERIFY_GH_LOG` resolves inside `VERIFY_ROOT`, and `VERIFY_ROOT/bin/gh` is the recording shim created by this run. If any check fails, do not run the installer; create a fresh scratch root.

## Drive

Use the installer command shape documented in `README.md` and `docs/commands.md`. Add `--from-local` to ensure Skill requests point to this checkout. Prefix every installer command with `PATH="$VERIFY_ROOT/bin:$PATH"` so it invokes the recording shim rather than the real GitHub CLI.

The mapped recipes are in `features/README.md`. For the standard smoke path, run:

```sh
PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile github --agent codex --scope project --target "$VERIFY_ROOT/project" --from-local
```

Require exit code `0`, stdout containing `Profiles: github`, and nonempty `$VERIFY_GH_LOG`. Check each request refers to a local Skill directory. `github` currently selects no Agent definitions, so do not expect `.omp/agents/` to be created. A repeat run records another set of requests; the shim verifies delegation only, not real `gh` idempotency.

## Evidence

Write evidence under `$VERIFY_ROOT/evidence/`. Capture the exact action/command, stdout, stderr, exit code, shim log, and sorted target-project file listing. Exercise the public installer with a real repository Profile and verify its external requests and filesystem effects. Source inspection and unit tests alone do not prove the user path.

The recording shim is allowed only at the external `gh skill install` boundary. Do not mock the installer, Profile resolution, or target filesystem writes. This proof verifies local request construction and installer behavior; it does not verify network access, authentication, or actual Skill installation. For a failed run, retain its command output for diagnosis.

## Cleanup

`artifacts/` is gitignored; copy proof outside the repository before sharing it because the directory is not tracked.

```sh
mkdir -p "$PWD/artifacts/verify-agent-capabilities"
cp -R "$VERIFY_ROOT/evidence/." "$PWD/artifacts/verify-agent-capabilities/"
rm -rf -- "$VERIFY_ROOT"
test -d "$PWD/artifacts/verify-agent-capabilities"
```

This run starts no server or long-lived process, so there is no process teardown. Remove only the scratch root created by this run. Never remove `artifacts/` during cleanup; proof must survive there. Keep proof out of commits unless requested.

## Helpers

No helper scripts are shipped. The executable shim and exact CLI invocation are shown above. Permanent installer tests run with `python3 -m unittest discover -s tests`; they supplement the CLI smoke drive.

## Feature map

Read `features/README.md` first, then follow the recipe matching the change. Verify all entry points listed for a feature before claiming that feature fully tested.
