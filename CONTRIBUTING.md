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

## Commit messages

Use [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages. The format is:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Use these types as the default vocabulary:

- `feat`: add a new feature
- `fix`: fix a bug
- `refactor`: change code without changing behavior
- `docs`: change documentation
- `test`: add or change tests
- `chore`: make maintenance changes
- `ci`: change continuous integration configuration
- `build`: change the build system or dependencies
- `perf`: improve performance
- `revert`: revert a previous change

Use a scope when it adds useful context, for example `fix(forecast): handle missing observations`.
Mark a breaking change with `!` after the type or scope, or with a `BREAKING CHANGE:` footer.

## Pull requests

Open a focused pull request with:

- a short summary of the change and its motivation;
- the affected Skills, Agents, Profiles, or catalog entries; and
- the verification commands and their results.

Keep external mutations explicit and scoped. Do not merge a pull request,
delete branches, or change repository settings unless that work is explicitly
authorized.
