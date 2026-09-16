# Contributing

This repository distributes reusable Codex Skills, Agents, and composable
Profiles. Keep contributions focused, portable, and consistent with the
existing capability boundaries.

## Before contributing

- Check the existing README, catalogs, Profiles, and related capabilities first.
- Keep specialist Skills narrow and model-selectable; do not add umbrella
  Skills for a language, database, OpenAPI, or GitHub workflow.
- Keep engineering capabilities under `packs/software-engineering/` and GitHub
  operations under `packs/operations/github/`.
- Reuse external Skills such as `$tdd`, `$code-review`, and `$gh-fix-ci`; do
  not copy or redefine them here.
- Do not include secrets, credentials, or personal data.

## Adding or changing capabilities

- Give every Skill a unique frontmatter `name` and a description that clearly
  states when it applies.
- Keep `SKILL.md`, Agent definitions, and Profile instructions in English so
  they remain portable across projects.
- Update the relevant README/catalog and Profile when adding or removing a
  capability. Update `docs/commands.md` when a capability introduces a
  concrete external CLI or changes a command family.
- Keep Profiles as distribution metadata; they are not another instruction
  layer.
- Prefer existing dependencies and repository conventions. Keep the diff
  small and avoid unrelated cleanup.

## Validation

From the repository root:

- Run `quick_validate.py` for every changed Skill directory.
- Check that Skill names are unique and all Profile selectors resolve.
- Run `git diff --check`.
- Run any additional checks relevant to the files changed and report what was
  run in the pull request.

## Pull requests

Open a focused pull request with:

- a short summary of the change and its motivation;
- the affected Skills, Agents, Profiles, or catalog entries; and
- the verification commands and their results.

Keep external mutations explicit and scoped. Do not merge a pull request,
delete branches, or change repository settings unless that work is explicitly
authorized.
