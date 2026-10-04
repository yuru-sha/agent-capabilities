import runpy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SYNC = runpy.run_path(str(ROOT / "scripts" / "sync-issue-automations"))
SYNC_GLOBALS = SYNC["main"].__globals__


class SyncIssueAutomationsTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.repo = Path(self.temporary_directory.name) / "repo"
        self.repo.mkdir()
        self.automation_dir = Path(self.temporary_directory.name) / "automations"
        self.automation_dir.mkdir()
        self.prompts = {}
        for key, _, _ in SYNC["DEFINITIONS"]:
            prompt = f"prompt for {key}\n"
            self.prompts[key] = prompt
            (self.automation_dir / f"{key}.md").write_text(prompt, encoding="utf-8")
        self.globals_patch = patch.dict(
            SYNC_GLOBALS,
            {"AUTOMATIONS": self.automation_dir},
        )
        self.globals_patch.start()
        self.addCleanup(self.globals_patch.stop)

    def record(self, key, name, automation_id, prompt, *, path=None, repo_id="repo-id"):
        return {
            "id": automation_id,
            "name": name,
            "prompt": prompt,
            "runContext": {"path": str(path or self.repo), "repoId": repo_id},
        }

    def invoke(self, repository, *extra_args):
        with patch("sys.argv", ["sync-issue-automations", "--repo", repository, *extra_args]):
            return SYNC["main"]()

    def test_existing_automation_is_updated_and_verified_for_id_selector(self):
        records = [
            self.record(key, name, f"id-{key}", "old prompt")
            for key, name, _ in SYNC["DEFINITIONS"]
        ]

        def run_orca(*args):
            if args == ("automations", "list"):
                return {"automations": records}
            if args[0:2] == ("automations", "edit"):
                return {}
            if args[0:2] == ("automations", "show"):
                key = args[2].removeprefix("id-")
                return {"automation": {"prompt": self.prompts[key]}}
            self.fail(f"unexpected Orca call: {args}")

        with patch.dict(SYNC_GLOBALS, {"run_orca": run_orca}), patch("sys.argv", [
            "sync-issue-automations", "--repo", "id:repo-id"
        ]):
            self.assertEqual(SYNC["main"](), 0)

    def test_existing_prompt_is_a_noop(self):
        records = [
            self.record(key, name, f"id-{key}", self.prompts[key])
            for key, name, _ in SYNC["DEFINITIONS"]
        ]
        calls = []

        def run_orca(*args):
            calls.append(args)
            return {"automations": records} if args == ("automations", "list") else {}

        with patch.dict(SYNC_GLOBALS, {"run_orca": run_orca}):
            self.assertEqual(self.invoke(str(self.repo)), 0)
        self.assertEqual(calls, [("automations", "list")])

    def test_handoff_activation_keeps_lifecycle_manual(self):
        records = [
            self.record(key, name, f"id-{key}", self.prompts[key])
            for key, name, _ in SYNC["DEFINITIONS"]
        ]
        records[0]["enabled"] = False
        records[1]["enabled"] = True
        calls = []

        def run_orca(*args):
            calls.append(args)
            if args == ("automations", "list"):
                return {"automations": records}
            if args[0:2] == ("automations", "edit"):
                next(item for item in records if item["id"] == args[2])["enabled"] = "--enabled" in args
                return {}
            if args[0:2] == ("automations", "show"):
                return {"automation": next(item for item in records if item["id"] == args[2])}
            self.fail(f"unexpected Orca call: {args}")

        with patch.dict(SYNC_GLOBALS, {"run_orca": run_orca}):
            self.assertEqual(self.invoke(str(self.repo), "--enable-handoff"), 0)
            handoff_enabled_states = [item["enabled"] for item in records]
            records[1]["enabled"] = True
            self.assertEqual(self.invoke(str(self.repo), "--disable-automations"), 0)
        self.assertEqual(handoff_enabled_states, [True, False])
        self.assertEqual([item["enabled"] for item in records], [False, False])
        self.assertIn(("automations", "edit", "id-issue-omp-handoff", "--enabled"), calls)
        self.assertIn(("automations", "edit", "id-issue-pr-lifecycle", "--disabled"), calls)
        self.assertIn(("automations", "edit", "id-issue-omp-handoff", "--disabled"), calls)

    def test_missing_automations_are_created_and_verified(self):
        created = []

        def run_orca(*args):
            if args == ("automations", "list"):
                return {"automations": []}
            if args[0:2] == ("automations", "create"):
                name = args[args.index("--name") + 1]
                key = next(key for key, definition_name, _ in SYNC["DEFINITIONS"] if definition_name == name)
                enabled = "--enabled" in args
                item = {
                    "id": f"new-{key}", "name": name, "prompt": self.prompts[key],
                    "enabled": enabled, "workspaceMode": "new_per_run",
                    "runContext": {"path": str(self.repo), "repoId": "repo-id"},
                }
                created.append(item)
                return {"automation": {"id": item["id"]}}
            if args[0:2] == ("automations", "show"):
                item = next(item for item in created if item["id"] == args[2])
                return {"automation": item}
            self.fail(f"unexpected Orca call: {args}")

        with patch.dict(SYNC_GLOBALS, {"run_orca": run_orca}):
            self.assertEqual(self.invoke(str(self.repo), "--provider", "omp", "--trigger", "daily"), 0)
        self.assertEqual([item["enabled"] for item in created], [True, False])
        self.assertEqual(len(created), 2)

    def test_id_selector_matches_repo_id_even_when_path_exists(self):
        record = self.record("handoff", "Issue OMP handoff", "automation", "prompt")
        self.assertTrue(SYNC["matches_repository"](record, "id:repo-id"))
        self.assertFalse(SYNC["matches_repository"](record, "id:another-repo"))


if __name__ == "__main__":
    unittest.main()
