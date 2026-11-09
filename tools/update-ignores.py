#!/usr/bin/env python3
"""Keep empty translation JSON files out of the playable pack."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
ignore = root / '.packwizignore'
marker = '# ----- >8 cut here - empty lang files ----- #'
text = ignore.read_text().split('# ----- >8 cut here')[0]
empty = []
for path in sorted((root / 'lang').rglob('*.json')):
    if json.loads(path.read_text()) == {}:
        empty.append(path.relative_to(root).as_posix())
ignore.write_text(text + marker + '\n' + '\n'.join(empty) + '\n')
