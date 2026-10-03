# Use GitHub workflow capabilities

Users select a workflow Profile to install GitHub operation Skills, then invoke a Skill by its documented name for the requested task.

## Sub-features

- `workflow-select` selects `github` for GitHub operation Skills or `workflows` for the full repository workflow set.
- `workflow-discover` finds a Skill's name and trigger scope from its frontmatter and instructions.
- `workflow-boundary` identifies approval requirements and operations excluded by the chosen Skill.

## How to get to it (user POV)

- Select `github` or `workflows` when running `scripts/install-profile`.
- Browse `packs/operations/github/skills/` and open a Skill's `SKILL.md` to find its invocation scope.
- Orca Automation prompts live under `packs/operations/github/automations/`; Profiles do not install them.

## Driving it with repository files

Preconditions:

- Run from the repository root.
- Read `profiles/github.yaml`, `profiles/workflows.yaml`, `profiles/README.md`, and the target Skill instructions; export `RUN_ID` so this run's evidence has its own subdirectory.

- **Select a workflow set.** Create a disposable target with `mkdir -p "$VERIFY_ROOT/workflows"`, then run `PATH="$VERIFY_ROOT/bin:$PATH" scripts/install-profile workflows --agent codex --scope project --target "$VERIFY_ROOT/workflows" --from-local`. Require exit code `0` and capture the shim requests.
- **Find an operation.** Open `packs/operations/github/skills/review-mode/SKILL.md`. Verify its frontmatter declares `name: review-mode`; read the instructions to identify its invocation scope and boundaries.
- **Distinguish Automation.** Open `packs/operations/github/automations/issue-omp-handoff.md`. Confirm this is an Orca Automation prompt, not an installable `SKILL.md` or a running service. Do not execute a GitHub or Orca mutation.

## Gotchas

- `workflows` includes GitHub pack Skills; `github` selects the GitHub-operation subset.
- Orca Automation prompts are not installed through `gh skill install`.
- Reading instructions verifies discovery and declared boundaries, not a live GitHub action. Do not report a PR, Issue, or Automation run as exercised by this recipe.
