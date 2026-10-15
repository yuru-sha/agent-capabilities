# Repository Guidelines

## Project Overview

This repository distributes reusable capabilities for AI coding agents: Skills, specialist Agent selectors, composable Profiles, and workflow instructions. Keep capabilities portable and independently selectable where useful; generic implementation workflow belongs to the consumer/OMP, not this repository.

## Architecture & Data Flow

- Packs define physical ownership: `packs/software-engineering/` for engineering capabilities and `packs/operations/github/` for GitHub operations and Orca Automation prompts.
- A Skill is a narrow selectable entry point. Its `SKILL.md` frontmatter (`name`, `description`) defines its identity and applicability; detailed topic guidance lives in `references/` and is loaded selectively.
- Profiles are distribution metadata, not another instruction layer. They select local or upstream Skill paths and Agent IDs.
- `scripts/install-profile` resolves selected Profiles, unions Skills, de-duplicates Agents by ID, installs Skills through `gh skill install`, and copies OMP Agent definitions separately. Do not assume those artifacts share an installation path.

## Key Directories

- `packs/`: reusable Skills, Agents, and workflow prompts, grouped by pack.
- `profiles/`: composable Profile YAML files and their usage guide.
- `scripts/`: repository validator, Profile installer, and automation synchronizer.
- `tests/`: standard-library `unittest` coverage of validation and scripts.
- `docs/`: catalogs, design notes, and external command reference.
- `.github/workflows/`: CI validation and repository automation.

## Development Commands

Run from the repository root:

```sh
python3 scripts/validate
python3 -m unittest discover -s tests
git diff --check
```

There is no separate build or configured lint/format command. Python 3.13 is used in CI; the documented maintenance scripts use Python 3 and the standard library.

## Code Conventions & Common Patterns

- Keep Skill, Agent, and Profile instruction text in English for portability; README/catalog text may use Japanese.
- Keep Skills focused: use a Skill for independently selectable capability; put concern-level detail in its parent Skill's `references/`. Avoid umbrella or compatibility-alias Skills.
- Keep Profiles declarative: compose paths/IDs; do not duplicate instructions there.
- When changing a capability, update the relevant Profile and catalog/README. Update `docs/commands.md` when adding or changing a required external CLI or command family.
- Keep external mutations explicit, scoped, and followed by verification. Avoid exposing secrets or personal data.
- Python script tests use isolated temporary directories, `unittest.mock`, and subprocess/shim smoke tests where appropriate.

### Code, Tests, Commits, and Comments

- Code should make how the behavior is implemented clear.
- Tests should make what behavior is expected clear.
- Commit messages should explain why the change is needed.
- Comments should explain why not an apparently reasonable alternative was chosen, including relevant constraints or non-obvious intent. Do not use comments to paraphrase the code's behavior.

## Important Files

- `README.md`, `README.ja.md`: capability overview, counts, and installation usage.
- `CONTRIBUTING.md`: contribution, commit, and PR requirements.
- `profiles/README.md`: Profile composition and installation conventions.
- `scripts/validate`: frontmatter, references, Profile resolution, and documented-count checks.
- `scripts/install-profile`: Profile resolution and installation behavior.
- `docs/commands.md`: human-facing command index, not a toolchain manifest.
- `.github/workflows/validate.yml`: CI validation, tests, and diff checks.

## Runtime/Tooling Preferences

Use Python 3 for repository maintenance scripts; CI uses Python 3.13. No package manager, dependency manifest, or runtime build step is required for repository checks. Capability-specific external CLIs are documented in `docs/commands.md`; consumer projects remain responsible for their own toolchain.

## Testing & QA

- `tests/test_validate.py` covers Skill metadata, local references, and Profile shape/resolution.
- `tests/test_install_profile.py` covers Profile composition, installation planning, conflicts, CLI behavior, and idempotency.
- `tests/test_install_profile_smoke.py` exercises the installer subprocess path using a temporary `gh` shim rather than the real external command.
- `tests/test_sync_issue_automations.py` covers automation synchronization.
- Add or update tests when behavior changes; run relevant checks above and report only those actually run. CI runs repository validation and the unittest suite.

## Contribution Workflow

- Work on a feature branch; do not edit, commit, or push directly to `main`. Do not commit unless explicitly requested.
- Do not merge pull requests, delete branches, or change repository settings unless explicitly authorized.
