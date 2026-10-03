import runpy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = runpy.run_path(str(ROOT / "scripts" / "install-profile"))
INSTALLER_GLOBALS = INSTALLER["load_profile"].__globals__


class InstallProfileTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)
        self.profiles = self.root / "profiles"
        self.skills = self.root / "skills"
        self.agents = self.root / "agent-definitions"
        self.profiles.mkdir()
        self.skills.mkdir()
        self.agents.mkdir()
        self.patch_globals = patch.dict(
            INSTALLER_GLOBALS,
            {
                "PROFILE_ROOT": self.profiles,
                "SOURCE_ROOT": self.root.resolve(),
                "AGENT_ROOT": self.agents,
            },
        )
        self.patch_globals.start()
        self.addCleanup(self.patch_globals.stop)

    def add_skill(self, directory, name, text="skill"):
        skill = self.root / directory
        skill.mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(f"---\nname: {name}\n---\n{text}\n", encoding="utf-8")
        return skill

    def add_agent(self, agent_id, content=None):
        path = self.agents / f"{agent_id}.md"
        path.write_text(content or f"Agent {agent_id}\n", encoding="utf-8")
        return path.resolve()

    def add_profile(self, profile_id, skills=(), agents=(), external=()):
        lines = [f"id: {profile_id}", "skills:", "  include:"]
        lines.extend(f"    - {selector}" for selector in skills)
        lines.extend(("agents:", "  include:"))
        lines.extend(f"    - {agent_id}" for agent_id in agents)
        lines.append("external_skills:")
        lines.extend(f"  - {skill}" for skill in external)
        (self.profiles / f"{profile_id}.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_profile_resolution_accepts_yaml_suffix_and_duplicate_input(self):
        self.add_skill("skills/alpha", "alpha")
        self.add_agent("planner")
        self.add_profile("go", ["skills/alpha"], ["planner"])
        profiles = INSTALLER["resolve_profiles"](["go.yaml", "go"])
        self.assertEqual([profile["id"] for profile in profiles], ["go"])
        self.assertEqual(tuple(profiles[0]["skills"]), ("alpha",))
        self.assertEqual(tuple(profiles[0]["agents"]), ("planner",))

    def test_repository_profiles_resolve_all_selectors(self):
        with patch.dict(
            INSTALLER_GLOBALS,
            {
                "PROFILE_ROOT": ROOT / "profiles",
                "SOURCE_ROOT": ROOT,
                "AGENT_ROOT": ROOT / "packs" / "software-engineering" / "agents",
            },
        ):
            profile_ids = sorted(path.stem for path in (ROOT / "profiles").glob("*.yaml"))
            plan = INSTALLER["build_install_plan"](profile_ids)

        self.assertEqual(plan.profile_ids, tuple(profile_ids))
        self.assertTrue(plan.skills)
        self.assertTrue(plan.agents)

    def test_union_plan_deduplicates_profiles_skills_agents_and_external_skills(self):
        self.add_skill("skills/alpha", "alpha")
        self.add_agent("planner")
        self.add_profile("one", ["skills/alpha"], ["planner"], ["vendor-skill"])
        self.add_profile("two", ["skills/alpha"], ["planner"], ["vendor-skill", "other-vendor"])

        plan = INSTALLER["build_install_plan"](["two", "one", "one"])

        self.assertEqual(plan.profile_ids, ("one", "two"))
        self.assertEqual([name for name, _ in plan.skills], ["alpha"])
        self.assertEqual([agent_id for agent_id, _ in plan.agents], ["planner"])
        self.assertEqual(plan.external_skills, ("other-vendor", "vendor-skill"))

    def test_conflicting_skill_name_from_distinct_sources_fails_before_side_effects(self):
        self.add_skill("skills/a", "shared")
        self.add_skill("skills/b", "shared")
        self.add_profile("one", ["skills/a"])
        self.add_profile("two", ["skills/b"])
        target = self.root / "target"
        target.mkdir()
        run = patch.object(INSTALLER["subprocess"], "run")
        with run as gh:
            with self.assertRaisesRegex(ValueError, "conflicting Skill"):
                plan = INSTALLER["build_install_plan"](["one", "two"])
                INSTALLER["install_profiles"](plan, agent="copilot", scope="project", target=target, from_local=False)
        gh.assert_not_called()
        self.assertFalse((target / ".omp").exists())

    def test_remote_project_install_uses_exact_skill_path_and_copies_agents(self):
        skill = self.add_skill("skills/alpha", "alpha")
        agent_source = self.add_agent("planner", "planner bytes\n")
        self.add_profile("one", ["skills/alpha"], ["planner"])
        target = self.root / "target"
        target.mkdir()
        plan = INSTALLER["build_install_plan"](["one"])
        remote_call = call(
            ["gh", "skill", "install", "yuru-sha/agent-capabilities", "skills/alpha/SKILL.md", "--agent", "copilot", "--scope", "project"],
            cwd=target,
            check=False,
        )
        with patch.object(INSTALLER["subprocess"], "run", return_value=type("Result", (), {"returncode": 0})()) as gh:
            result = INSTALLER["install_profiles"](plan, agent="copilot", scope="project", target=target, from_local=False)

        self.assertEqual(result, 0)
        gh.assert_called_once_with(*remote_call.args, **remote_call.kwargs)
        self.assertFalse(any(str(skill) in str(arg) for arg in gh.call_args.args[0]))
        self.assertEqual((target / ".omp" / "agents" / "planner.md").read_bytes(), agent_source.read_bytes())


    def test_omp_host_maps_to_universal_for_gh_skill_install(self):
        skill = self.add_skill("skills/alpha", "alpha")
        plan = INSTALLER["InstallPlan"](("one",), (("alpha", skill),), (), ())
        with patch.object(INSTALLER["subprocess"], "run", return_value=type("Result", (), {"returncode": 0})()) as gh:
            result = INSTALLER["install_profiles"](plan, agent="omp", scope="project", target=self.root, from_local=True)

        self.assertEqual(result, 0)
        self.assertEqual(gh.call_args.args[0][gh.call_args.args[0].index("--agent") + 1], "universal")

    def test_local_install_uses_skill_directory_as_source(self):
        skill = self.add_skill("skills/alpha", "alpha")
        self.add_profile("one", ["skills/alpha"])
        target = self.root / "target"
        target.mkdir()
        plan = INSTALLER["build_install_plan"](["one"])
        with patch.object(INSTALLER["subprocess"], "run", return_value=type("Result", (), {"returncode": 0})()) as gh:
            INSTALLER["install_profiles"](plan, agent="claude-code", scope="project", target=target, from_local=True)

        gh.assert_called_once_with(
            ["gh", "skill", "install", str(skill.resolve()), "alpha", "--from-local", "--agent", "claude-code", "--scope", "project"],
            cwd=target,
            check=False,
        )

    def test_user_install_targets_expanded_home_and_rejects_different_existing_agent(self):
        agent_source = self.add_agent("planner", "expected\n")
        self.add_profile("one", agents=["planner"])
        plan = INSTALLER["build_install_plan"](["one"])
        destination = Path.home() / ".omp" / "agent" / "agents" / "planner.md"
        with patch.object(INSTALLER["Path"], "home", return_value=self.root / "home"):
            home_destination = self.root / "home" / ".omp" / "agent" / "agents" / "planner.md"
            home_destination.parent.mkdir(parents=True)
            home_destination.write_bytes(agent_source.read_bytes())
            destinations = INSTALLER["agent_destinations"](plan, "user", None)
            self.assertEqual(destinations[0][0], home_destination)
            INSTALLER["preflight_agents"](destinations)
            home_destination.write_text("different\n", encoding="utf-8")
            with patch.object(INSTALLER["subprocess"], "run") as gh:
                with self.assertRaisesRegex(ValueError, "Agent destination conflict"):
                    INSTALLER["install_profiles"](plan, agent="copilot", scope="user", target=None, from_local=False)
                gh.assert_not_called()
        self.assertNotEqual(destination, home_destination)

    def test_identical_existing_agent_is_idempotent_and_nonzero_gh_stops(self):
        agent_source = self.add_agent("planner", "same\n")
        self.add_skill("skills/alpha", "alpha")
        self.add_profile("one", ["skills/alpha"], ["planner"])
        target = self.root / "target"
        target.mkdir()
        destination = target / ".omp" / "agents" / "planner.md"
        destination.parent.mkdir(parents=True)
        destination.write_bytes(agent_source.read_bytes())
        plan = INSTALLER["build_install_plan"](["one"])
        failed = type("Result", (), {"returncode": 7})()
        with patch.object(INSTALLER["subprocess"], "run", return_value=failed) as gh:
            with patch("sys.stderr"):
                result = INSTALLER["install_profiles"](plan, agent="copilot", scope="project", target=target, from_local=False)
        self.assertEqual(result, 7)
        gh.assert_called_once()
        self.assertEqual(destination.read_bytes(), agent_source.read_bytes())

    def test_cli_requires_host_and_scope_and_rejects_user_target(self):
        with self.assertRaises(SystemExit) as missing:
            INSTALLER["parse_args"](["go"])
        self.assertEqual(missing.exception.code, 2)
        with self.assertRaises(SystemExit) as invalid:
            INSTALLER["parse_args"](["go", "--agent", "copilot", "--scope", "user", "--target", "."])
        self.assertEqual(invalid.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
