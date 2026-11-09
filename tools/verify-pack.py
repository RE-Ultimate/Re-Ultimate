#!/usr/bin/env python3
"""Check the published manifest against the actual checkout, including hydrated LFS files."""
import hashlib
import tomllib
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parent.parent
pack = tomllib.loads((root / 'pack.toml').read_text())
index_path = root / pack['index']['file']
assert hashlib.new(pack['index']['hash-format'], index_path.read_bytes()).hexdigest() == pack['index']['hash'], 'pack.toml index hash'
index = tomllib.loads(index_path.read_text())
for entry in index['files']:
    path = root / entry['file']
    content = path.read_bytes()
    assert not content.startswith(b'version https://git-lfs.github.com/spec/v1'), 'Run git lfs pull: ' + entry['file']
    algorithm = entry.get('hash-format', index['hash-format'])
    assert hashlib.new(algorithm, content).hexdigest() == entry['hash'], entry['file']
    if entry.get('metafile'):
        data = tomllib.loads(content.decode())
        url = data.get('download', {}).get('url')
        if url:
            host = urlsplit(url).hostname
            assert host not in {'rewindmc.com', 'repo.sleeping.town', 'git.sleeping.town'}, 'Old distribution host: ' + entry['file']
assert pack['name'] == 'Re:Ultimate'
assert any(entry['file'] == 'nilmods/EMI.jar' for entry in index['files']), 'EMI is missing'
assert not any(entry['file'] in {'coremods/notenoughitems.pw.toml', 'mods/NEIPlugins.jar', 'mods/nei-redpower-plugin.pw.toml'} for entry in index['files']), 'Superseded NEI integration is present'
print('Verified', len(index['files']), 'pack entries for', pack['name'], pack['version'])
