import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InstallProfileSmokeTests(unittest.TestCase):
    def test_from_local_cli_uses_gh_shim_without_external_mutation(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary = Path(temporary_directory)
            target = temporary / "target"
            target.mkdir()
            bin_dir = temporary / "bin"
            bin_dir.mkdir()
            log = temporary / "gh.log"
            gh = bin_dir / "gh"
            gh.write_text(
                "#!/usr/bin/env python3\n"
                "import os, sys\n"
                "with open(os.environ['GH_SHIM_LOG'], 'a', encoding='utf-8') as handle:\n"
                "    handle.write(' '.join(sys.argv[1:]) + '\\n')\n"
                "raise SystemExit(0)\n",
                encoding="utf-8",
            )
            gh.chmod(0o755)

            env = os.environ.copy()
            env["GH_SHIM_LOG"] = str(log)
            env["PATH"] = str(bin_dir) + os.pathsep + env.get("PATH", "")

            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install-profile"),
                    "meta-marketing",
                    "--agent",
                    "universal",
                    "--scope",
                    "project",
                    "--target",
                    str(target),
                    "--from-local",
                ],
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Profiles: meta-marketing", result.stdout)
            calls = log.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(calls), 1)
            self.assertIn("skill install", calls[0])
            self.assertIn("meta-marketing-api", calls[0])
            self.assertIn("--from-local", calls[0])
            self.assertIn("--agent universal", calls[0])
            self.assertIn("--scope project", calls[0])


if __name__ == "__main__":
    unittest.main()
