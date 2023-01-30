<center><img height="192" src="https://rewindmc.com/upsilon-full.png"></center>

**[Rewind](https://rewindmc.com) is a project to create "retro" modpacks for significant past versions
of Minecraft.** It aims to provide a definitive and less buggy experience,
including backports of some modern conveniences (such as item smearing and ctrl
sprint) and retromods that didn't exist back in the day.

**WARNING:** Rewind Upsilon is still an experimental beta! Please [report issues](https://git.sleeping.town/unascribed/RewindUpsilon/issues),
and take regular backups!

Rewind packs are compatible with the major FTB pack from their same version. You
can load an FTB Ultimate world in Rewind Upsilon and it will upgrade seamlessly.
You just get a less buggy and more featureful experience.

So, why? It's pretty simple: these old versions of modded Minecraft are quite
unique on their own, especially compared to modern modded, and the experiences
offered by them still hold up today. Rewind packs are for anyone that wishes to
revisit older versions of modded Minecraft, nostalgia or no. Playing a Rewind
pack shields you from many known bugs, ranging from mild inconveniences, to game
crashes, to dangerous remote code execution vulnerabilities. Additionally, all
the mods are fixed to work on modern Java 8 and disable all reliance on
long-gone servers.

Upsilon is Rewind's flagship pack (and first pack), built for Minecraft 1.4.7.
It is also the first ever modpack to use [NilLoader](https://git.sleeping.town/unascribed/NilLoader).

## Differences from FTB Ultimate
- Updated BuildCraft to 3.4.5
  - The Builder is disabled by default, as in 3.4.3 and 3.4.4, but can be enabled in the BuildCraft config (use caution)
- Added Ears
- Added LegacyCustomPublish
- Added LogisticsPipes
- Added DartCraft
- Added Chisel Retro
- Added FallingFix
- Updated GregTech
- Removed ForgeIRC
- New panorama (seed is 8718729173668754797 at 156, 97, 86)
- Enabled all EBXL biomes
- PowerConverters is disabled by default
- Added SplashAnimation (a custom backport)
- Custom loading animation
- Added NilLoader
- Added Flamingo
- Added RPTweaks
  - Fixes Canvas Bag item duplication
  - Fixes screwdrivers not changing bus IDs
  - Fixes RedPower blocks dropping when broken in Creative
  - Fixes some blocks dropping twice
  - Adds a Clear button to the Project Table
  - Fixes crashes when opening a logic tile GUI while holding a block

All of the following are done by UpsilonFixes, and can be disabled in its config:
- **Fixed water whirlpools (backported 1.5 water fill behavior) ([MC-916](https://bugs.mojang.com/browse/MC-916))**
- **PortalGun sounds fixed**
- **Fixed EE3 Minium stone recipes being broken after using them once or after NEI recipe lookup**
- **Items can be dragged over slots to spread them out (1.5 backport)**
- Double/triple-clicking a slot will collect all items of that type to your cursor (1.5 backport)
- Holding the IC2 Boost Key (lctrl by default) will cause you to sprint
- Pressing the drop key over a slot in an inventory will drop the item in that slot (1.5 backport)
- Fixed attacker yaw not syncing to fix the camera tilt animation ([MC-26678](https://bugs.mojang.com/browse/MC-26678))
- Re-enabled SHA-1 signing algorithm in Java to fix mods crashing with signature errors on current Java 8 patches
- Texture packs can change the font
- Added "layerable" texture packs
- Fixed RP2 lamp hitboxes
- Fixed missing lang entry for Thaumic Bees' Rejuvenating bee effect
- Flux bees can provide Aer
- IC2 capes removed as they contact a broken URL and are obfuscated
- XyCraft quartz crystal generation disabled to improve performance
- NEIPlugins update check removed
- Applied Energistics update check removed
- CoFH update check removed
- BuildCraft update check removed
- MFFS update check removed
- GregTech capes removed as they contact broken Dropbox links
- Steve's Carts capes removed for the same reason
- Fixed MiscPeripherals ASM API misuse
- Added Rewind Upsilon logo to main menu
- Fixed LiteLoader logger to look consistent with the Forge one
- Fixed a CodeChickenCore transformer bug (only really visible alongside NilLoader)
- Nilmods are shown in VoxelMenu Mod Info
- Patched ObjectWeb ASM to not explode on Java 8 classes
