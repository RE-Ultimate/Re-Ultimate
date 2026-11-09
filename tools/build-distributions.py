#!/usr/bin/env python3
"""Build clean Prism and server bootstrap archives; no personal instance files are copied."""
import json
import subprocess
import sys
import tomllib
import urllib.request
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
subprocess.run([sys.executable, str(root / 'tools/verify-pack.py')], check=True)
version = tomllib.loads((root / 'pack.toml').read_text())['version']
feed = 'https://re-ultimate.github.io/Re-Ultimate/pack.toml'
maven = 'https://raw.githubusercontent.com/RE-Ultimate/maven/main'
out = root / 'dist'
out.mkdir(exist_ok=True)


def archive(path, files):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if name.endswith('.sh') else 0o100644) << 16
            z.writestr(info, data.encode() if isinstance(data, str) else data)
    print('Created', path)


ini = f'''version=1
preset=minecraft
source_format=packwiz
source={feed}
update_mmc_pack=true
'''
client = {
    'instance.cfg': 'InstanceType=OneSix\nname=Re:Ultimate\niconKey=reultimate\n',
    'icon.png': (root / 'icon.png').read_bytes(),
    'reultimate.png': (root / 'icon.png').read_bytes(),
    '.minecraft/unsup.ini': ini,
    'mmc-pack.json': json.dumps({'formatVersion': 1, 'components': [
        {'uid': 'net.minecraft', 'version': '1.4.7'},
        {'uid': 'net.minecraftforge', 'version': '6.6.2.534'},
        {'uid': 'com.unascribed.unsup', 'version': '1.2.7'},
        {'uid': 'com.unascribed.nilloader', 'version': '1.3.5'}]}, indent=2),
}
for artifact, agent_version, display in [('unsup', '1.2.7', 'unsup'), ('nilloader', '1.3.5', 'NilLoader')]:
    client[f'patches/com.unascribed.{artifact}.json'] = json.dumps({
        'formatVersion': 1, 'name': display, 'uid': 'com.unascribed.' + artifact,
        'version': agent_version, '+agents': [{'name': f'com.unascribed:{artifact}:{agent_version}', 'url': maven + '/'}]}, indent=2)
archive(out / f'Re-Ultimate-{version}-prism.zip', client)

with urllib.request.urlopen(maven + '/com/unascribed/unsup/1.2.7/unsup-1.2.7.jar', timeout=120) as response:
    updater = response.read()
server = {
    'unsup.jar': updater,
    'unsup.ini': ini.replace('update_mmc_pack=true', 'update_mmc_pack=false') + '\nforce_env=server\n\n[flavors]\nflavor=standard\ngregtech=gregtech_on\ndartcraft=dartcraft_on\n',
    'start.sh': '''#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
java -Djava.awt.headless=true -jar unsup.jar
exec java -Xms512M -Xmx4G -javaagent:nilloader.jar -jar forge.jar nogui
''',
    'start.bat': '@echo off\r\ncd /d "%~dp0"\r\njava -Djava.awt.headless=true -jar unsup.jar\r\nif errorlevel 1 exit /b %errorlevel%\r\njava -Xms512M -Xmx4G -javaagent:nilloader.jar -jar forge.jar nogui\r\n',
    'README.txt': 'Re:Ultimate ' + version + '\nUse Java 8. Run start.sh or start.bat.\nhttps://github.com/RE-Ultimate/Re-Ultimate\n',
    'LICENSE': (root / 'LICENSE').read_text(),
    'THIRD_PARTY.md': (root / 'THIRD_PARTY.md').read_text(),
}
archive(out / f'Re-Ultimate-{version}-server.zip', server)
