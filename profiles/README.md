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

`external_skills` names existing global Skills such as `$tdd` and
`$code-review`; the profiles do not copy or redefine them.
