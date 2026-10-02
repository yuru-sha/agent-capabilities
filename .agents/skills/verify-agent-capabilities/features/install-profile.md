# Install a Profile

A maintainer or consumer runs the Profile installer to install the selected Skills and copy any selected OMP Agent definitions into a project or user destination.

## Sub-features

- `install-project` installs a Profile into a project target.
- `install-local` uses Skill sources from this checkout.
- `install-repeat` reruns against an existing target.

## How to get to it (user POV)

- Run `scripts/install-profile <profile> --agent <host> --scope project` from this repository.
- Add `--target <directory>` to choose the project and `--from-local` to use this checkout's Skill sources.

## Driving it with the installer CLI

Preconditions:

- Follow `../SKILL.md` Launch and Doctor; export `RUN_ID` from Launch so evidence lands in its own subdirectory.
- Use the recording `gh` shim and an empty temporary project target.
- Run from the repository root.

- **Install GitHub Profile.** Run `PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile github --agent codex --scope project --target "$VERIFY_ROOT/project" --from-local`. Require exit code `0`, stdout `Profiles: github`, and one shim log line per resolved Skill.
- **Inspect side effects.** Check the target file listing and compare any `.omp/agents/` files with the Agent selectors in `profiles/github.yaml`. This Profile currently selects no Agents. Check the shim log for local Skill paths.
- **Repeat.** Run the exact same command. Require exit code `0`. The shim records the delegated requests again; this does not test actual GitHub CLI installation idempotency.

## Gotchas

- `--from-local` changes the source of Skill requests. Profile metadata always comes from this checkout.
- The shim records arguments, not the behavior of real `gh skill install`.
- `--scope user` writes under the real home directory; do not use it here.
- A Profile with no Agent selectors does not create `.omp/agents/`.
