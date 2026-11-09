#!/usr/bin/env python3
"""Stage the update feed without Git metadata or local build output."""
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
subprocess.run([sys.executable, str(root / 'tools/verify-pack.py')], check=True)
destination = Path(sys.argv[1] if len(sys.argv) > 1 else root / 'site').resolve()
if destination.exists():
    raise SystemExit('Destination already exists: ' + str(destination))
shutil.copytree(root, destination, ignore=shutil.ignore_patterns('.git', '.github', '.woodpecker', 'tools', 'docs', 'branding', 'site', 'dist', '__pycache__'))
(destination / '.nojekyll').touch()
print('Staged update feed at', destination)
