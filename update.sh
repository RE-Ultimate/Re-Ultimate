#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 tools/update-ignores.py
packwiz refresh
python3 tools/verify-pack.py
