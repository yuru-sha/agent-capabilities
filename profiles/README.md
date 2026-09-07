# Profiles

Profiles are composable distribution metadata. They select Skills and Agents;
they are not additional `SKILL.md` files and are not loaded as instructions.

For a Go project using SQLite, the consumer selects:

```yaml
profiles:
  - go
  - sqlite
```

The resolver takes the union of the selected Skill paths and de-duplicates
Agents by ID. `go+sqlite` is a generated bundle name, not a source Profile.

The `workflows` Profile contains the GitHub lifecycle Skills for commit/push,
ready and draft pull requests, Copilot review requests, releases, security
alerts, issue creation, and post-merge cleanup.

The `github` Profile selects only the GitHub-hosted collaboration, release, and
security-alert Skills. It declares the official global `$gh-fix-ci` Skill as an
external dependency and does not copy it.

`external_skills` names existing global Skills such as `$tdd` and
`$code-review` and `$gh-fix-ci`; the profiles do not copy or redefine them.
