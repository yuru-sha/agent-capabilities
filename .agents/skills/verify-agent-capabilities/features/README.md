# agent-capabilities verification map

This repository distributes Skills, Agent selectors, Profiles, and Orca Automation prompts. It has no long-running application. Read the `verify-agent-capabilities` Skill for the isolated installer launch, doctor, evidence, and cleanup procedure. The smoke drive runs the real `scripts/install-profile` CLI and uses a recording shim only at the external `gh skill install` boundary.

## Baseline preconditions

- Run from the repository root.
- Create a unique temporary `VERIFY_ROOT` with `bin/gh`, `project/`, and `evidence/` as documented in the Skill.
- Use `--from-local`; never install into a real consumer project during verification.
- Run the Skill's doctor before driving.

## Driving conventions

- Use the exact CLI commands and setup steps in the feature files.
- Save command, stdout, stderr, exit code, target file listing, and external request log under `$VERIFY_ROOT/evidence/`.
- The recording `gh` shim prevents GitHub mutations. It verifies only delegated arguments, not real authentication or installation.
- `artifacts/` is gitignored; set the unique `RUN_ID` in the Skill's Launch step and copy proof to `$PWD/artifacts/verify-agent-capabilities/$RUN_ID/` before cleanup.

## Features

- [Install a Profile](./install-profile.md) covers local project-scope installation and repeated invocation.
- [Resolve and compose Profiles](./resolve-profiles.md) covers single and combined Profile resolution and invalid selectors.
- [Use GitHub workflow capabilities](./github-workflows.md) covers workflow Skill discovery and documented invocation boundaries.
