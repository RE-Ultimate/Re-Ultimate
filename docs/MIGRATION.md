# Migration to RE-Ultimate

The source forks include the original available commit histories and authors. The modpack, translations, and unsup histories used SHA-256 Git objects; GitHub requires SHA-1, so their Git commit IDs changed during import. Git LFS object hashes did not change.

The original current pack LFS files were recovered and verified. Historical LFS objects were fetched before publishing. The current translations were recovered in full. Two historical translation commits no longer exist on the original server: `22346e68a8679dd22fcdeb14b264e4f0183f26dd755da73a5535598678aef9c4` and `d3f96b959b8d1cd633fdb6870ea5b3082c6f19391efc0418f49fb60602c4d26c`. They have explicit empty placeholder commits in `translations`, under `archive/unavailable/*`; no translation content was invented for them.

The original pack's root snapshot had no license file. The MIT license in this fork covers Re:Ultimate's new maintenance scripts, documentation, and branding. It does not relicense upstream pack files, translations, mods, music, loader, or updater. Component notices remain in place.

The original `com.rewindmc` Java package names, mod IDs, channels, configuration keys, and the `UpsilonFixes.jar` installation path remain for compatibility. The displayed names, main-menu links, launcher name, loading screen, update feed, build bootstrap, and Maven host now use Re:Ultimate.

The previous `unsup.sig` signed a different manifest and was removed. These initial updater templates, like the previous play setup, do not configure a pack public key. Distribution uses HTTPS and per-file hashes; this is not a signed-pack release.
