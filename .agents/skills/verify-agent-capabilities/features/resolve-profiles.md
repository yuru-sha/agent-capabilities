# Resolve and compose Profiles

Users choose Profile IDs to install named capability sets. The installer resolves their Skills, Agent selectors, and external Skill requirements before installing anything.

## Sub-features

- `resolve-single` resolves one repository Profile.
- `resolve-union` combines Profiles and de-duplicates resolved capabilities.
- `resolve-invalid` rejects unknown Profiles before installation side effects.

## How to get to it (user POV)

- Select Profile IDs as positional arguments to `scripts/install-profile`.
- Consult `profiles/README.md` and `profiles/*.yaml` to find supported Profile names and composition.

## Driving it with the installer CLI

Preconditions:

- Follow `../SKILL.md` Launch and Doctor; export `RUN_ID` from Launch so evidence lands in its own subdirectory.
- Create a fresh scratch root and recording `gh` shim.
- Run from the repository root.

- **Resolve one Profile.** Run `PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile github --agent codex --scope project --target "$VERIFY_ROOT/project" --from-local`. Require exit code `0` and stdout `Profiles: github`.
- **Compose Profiles.** Create the target with `mkdir -p "$VERIFY_ROOT/combined"`, then run `PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile go sqlite --agent codex --scope project --target "$VERIFY_ROOT/combined" --from-local`. Require exit code `0` and stdout `Profiles: go, sqlite`. Compare requests for this invocation with the union of the two Profile selectors; duplicate Skill names must be requested once.
- **Reject an unknown Profile.** Create the target with `mkdir -p "$VERIFY_ROOT/invalid"`, then run `PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile unknown-profile --agent codex --scope project --target "$VERIFY_ROOT/invalid" --from-local`. Require nonzero exit with `unknown profile` on stderr; verify the shim log did not grow and no Agent files were copied.

## Gotchas

- Resolution validates selectors before external installation begins.
- Profile IDs in output are sorted, not necessarily in argument order.
- A failing real `gh` call can leave earlier Skills installed; use only the recording shim and disposable targets.
