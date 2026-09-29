import runpy
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = runpy.run_path(str(ROOT / "scripts" / "install-profile"))


class InstallProfileUpgradeTests(unittest.TestCase):
    def install_go(self, target, *, link):
        profiles = INSTALLER["resolve_profiles"](["go"])
        self.assertEqual(
            INSTALLER["install_profiles"](target, profiles, link=link, force=False),
            0,
        )

    def add_legacy_entry(
        self,
        target,
        relative_path,
        source,
        mode,
        content,
        profile_ids=("go",),
    ):
        destination = target / relative_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if mode == "linked":
            destination.symlink_to(source, target_is_directory=True)
        else:
            destination.write_text(content, encoding="utf-8")

        manifest = INSTALLER["load_manifest"](target)
        for profile_id in profile_ids:
            manifest["profiles"].setdefault(profile_id, []).append(relative_path)
        manifest["entries"][relative_path] = {
            "source": str(source),
            "mode": mode,
            "kind": "agent",
        }
        INSTALLER["save_manifest"](target, manifest)
        return destination

    def test_removed_copy_missing_source_stays_tracked_until_force(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            self.install_go(target, link=True)
            legacy_path = ".codex/agents/planner.md"
            destination = self.add_legacy_entry(
                target,
                legacy_path,
                ROOT / "packs/software-engineering/agents/planner.md",
                "copied",
                "previously installed agent",
            )

            self.install_go(target, link=True)
            upgraded_manifest = INSTALLER["load_manifest"](target)
            self.assertTrue(destination.is_file())
            self.assertIn(legacy_path, upgraded_manifest["profiles"]["go"])

            self.assertEqual(
                INSTALLER["uninstall_profiles"](target, ["go"], force=True),
                0,
            )
            self.assertFalse(destination.exists())

    def test_modified_copy_stays_owned_until_forced_uninstall(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            self.install_go(target, link=False)
            legacy_path = ".codex/agents/legacy.md"
            source = target / "old-agent-source.md"
            source.write_text("original agent", encoding="utf-8")
            destination = self.add_legacy_entry(
                target, legacy_path, source, "copied", "user-modified agent"
            )

            self.install_go(target, link=False)
            manifest = INSTALLER["load_manifest"](target)
            self.assertEqual(
                destination.read_text(encoding="utf-8"),
                "user-modified agent",
            )
            self.assertIn(legacy_path, manifest["profiles"]["go"])

            self.assertEqual(
                INSTALLER["uninstall_profiles"](target, ["go"], force=False),
                0,
            )
            self.assertTrue(destination.exists())
            self.assertIn(
                legacy_path,
                INSTALLER["load_manifest"](target)["profiles"]["go"],
            )

            self.assertEqual(
                INSTALLER["uninstall_profiles"](target, ["go"], force=True),
                0,
            )
            self.assertFalse(destination.exists())

    def test_removed_link_to_missing_source_is_cleaned_during_upgrade(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            self.install_go(target, link=True)
            legacy_path = ".agents/skills/old-agent"
            source = target / "removed-sources" / "old-agent"
            destination = self.add_legacy_entry(
                target, legacy_path, source, "linked", ""
            )
            self.assertTrue(destination.is_symlink())

            self.install_go(target, link=True)
            self.assertFalse(destination.is_symlink())
            self.assertNotIn(
                legacy_path,
                INSTALLER["load_manifest"](target)["profiles"]["go"],
            )

    def test_obsolete_entry_shared_with_another_profile_is_preserved(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            self.install_go(target, link=True)
            legacy_path = ".agents/skills/shared-old-skill"
            destination = self.add_legacy_entry(
                target,
                legacy_path,
                target / "removed-sources" / "old-skill",
                "copied",
                "shared skill",
                profile_ids=("go", "sqlite"),
            )

            self.install_go(target, link=True)
            manifest = INSTALLER["load_manifest"](target)
            self.assertTrue(destination.is_file())
            self.assertNotIn(legacy_path, manifest["profiles"]["go"])
            self.assertIn(legacy_path, manifest["profiles"]["sqlite"])
            self.assertIn(legacy_path, manifest["entries"])


if __name__ == "__main__":
    unittest.main()
