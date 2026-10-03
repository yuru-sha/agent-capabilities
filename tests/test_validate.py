import runpy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = runpy.run_path(str(ROOT / "scripts" / "validate"))
GLOBALS = VALIDATOR["validate_skills"].__globals__


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)

    def test_frontmatter_requires_name_and_description(self):
        skill = self.root / "SKILL.md"
        skill.write_text("---\nname: alpha\n---\n# Alpha\n", encoding="utf-8")

        fields, problems = VALIDATOR["parse_frontmatter"](skill)

        self.assertEqual(fields["name"], "alpha")
        self.assertEqual(problems, [])

        with patch.dict(GLOBALS, {"ROOT": self.root, "SKILL_ROOTS": (self.root,)}):
            problems = VALIDATOR["validate_skills"]()

        self.assertTrue(any("description" in problem.message for problem in problems))

    def test_duplicate_skill_names_are_rejected(self):
        for directory in ("a", "b"):
            path = self.root / directory
            path.mkdir()
            (path / "SKILL.md").write_text(
                "---\nname: shared\ndescription: Shared test Skill description.\n---\n",
                encoding="utf-8",
            )

        with patch.dict(GLOBALS, {"ROOT": self.root, "SKILL_ROOTS": (self.root,)}):
            problems = VALIDATOR["validate_skills"]()

        self.assertTrue(any("duplicate Skill name" in problem.message for problem in problems))

    def test_broken_relative_link_is_rejected(self):
        skill = self.root / "SKILL.md"
        skill.write_text(
            "---\nname: alpha\ndescription: Alpha test Skill description.\n---\n"
            "[missing](references/missing.md)\n",
            encoding="utf-8",
        )

        with patch.dict(GLOBALS, {"ROOT": self.root}):
            problems = VALIDATOR["validate_local_links"](skill)

        self.assertEqual(len(problems), 1)
        self.assertIn("broken local link", problems[0].message)

    def test_existing_relative_link_is_accepted(self):
        references = self.root / "references"
        references.mkdir()
        (references / "current.md").write_text("# Current\n", encoding="utf-8")
        skill = self.root / "SKILL.md"
        skill.write_text("[current](references/current.md)\n", encoding="utf-8")

        with patch.dict(GLOBALS, {"ROOT": self.root}):
            problems = VALIDATOR["validate_local_links"](skill)

        self.assertEqual(problems, [])

    def test_profile_shape_rejects_unknown_structure(self):
        profile = self.root / "alpha.yaml"
        profile.write_text(
            "schema: 1\n"
            "id: alpha\n"
            "kind: integration\n"
            "description: Alpha integration profile.\n"
            "skills:\n"
            "  include:\n"
            "    - skills/alpha\n"
            "unknown: true\n",
            encoding="utf-8",
        )

        problems = VALIDATOR["validate_profile_shape"](profile)

        self.assertTrue(any("unsupported Profile key" in problem.message for problem in problems))

    def test_profile_shape_accepts_repository_format(self):
        profile = self.root / "alpha.yaml"
        profile.write_text(
            "schema: 1\n"
            "id: alpha\n"
            "kind: integration\n"
            "description: Alpha integration profile.\n"
            "\n"
            "skills:\n"
            "  include:\n"
            "    - skills/alpha/**\n"
            "\n"
            "agents:\n"
            "  include: []\n",
            encoding="utf-8",
        )

        self.assertEqual(VALIDATOR["validate_profile_shape"](profile), [])


if __name__ == "__main__":
    unittest.main()
