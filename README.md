# Re:Ultimate

A maintained Minecraft 1.4.7 modpack based on Rewind Upsilon and FTB Ultimate.

This fork includes the MFR duplicate-enchantment fix, expanded retroEMI integrations, AE1 recipe filling from ME storage, taller terminals, and the dedicated-server crafting crash fix.
Original project history and credits are retained in [the upstream notes](docs/UPSTREAM.md).

## Install

Download a client or server archive from [Releases](https://github.com/RE-Ultimate/Re-Ultimate/releases).
Import the Prism archive into Prism Launcher and select a Java 8 runtime.
For a server, extract the server archive, select Java 8, and run `start.sh` or `start.bat`.

The updater reads [https://re-ultimate.github.io/Re-Ultimate/pack.toml](https://re-ultimate.github.io/Re-Ultimate/pack.toml).
It uses this organization's feed and pinned dependencies; no account on the original Git server is required.
Existing world and mod identifiers are retained. Keep backups before changing an existing installation.

## Repositories

| Repository | Purpose |
| --- | --- |
| [UltimateFixes](https://github.com/RE-Ultimate/UltimateFixes) | Fixes, backports, and game branding |
| [retroEMI](https://github.com/RE-Ultimate/retroEMI) | Recipes, crafting transfer, and AE1 terminal UI |
| [translations](https://github.com/RE-Ultimate/translations) | Mod translations |
| [NilLoader](https://github.com/RE-Ultimate/NilLoader) and [NilGradle](https://github.com/RE-Ultimate/NilGradle) | Loader and build tooling |
| [UnknownThingy](https://github.com/RE-Ultimate/UnknownThingy) | Minecraft mappings |
| [unsup](https://github.com/RE-Ultimate/unsup) | Updater source |
| [maven](https://github.com/RE-Ultimate/maven) | Pinned build and launcher artifacts |

## Maintain

Install Git LFS, Python 3.11 or newer, and [packwiz](https://packwiz.infra.link/).

```sh
git clone --recurse-submodules https://github.com/RE-Ultimate/Re-Ultimate.git
cd Re-Ultimate
git lfs pull
./update.sh
python3 tools/verify-pack.py
python3 tools/build-distributions.py
```

Commit the refreshed `pack.toml` and `index.toml` together. Pushes to `main` publish the pack feed through GitHub Pages.
Build new fixes and EMI JARs in their source repositories, copy them to `nilmods/UpsilonFixes.jar` and `nilmods/EMI.jar`, then refresh the pack.

See [migration details](docs/MIGRATION.md), [integration coverage](https://github.com/RE-Ultimate/retroEMI/blob/main/docs/upsilon-integration.md), and [component licenses](THIRD_PARTY.md).
