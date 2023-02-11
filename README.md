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

Rewind Upsilon will be released on Modrinth once some redistribution issues are
sorted out. You can try the beta right now in Prism Launcher by [importing this instance zip](https://rewindmc.com/dl/upsilon.zip)
— that version uses unsup to download mods from their original sources. You can
also [download this zip](https://rewindmc.com/dl/upsilon-server.zip) to run a server,
with full updater support.

## Differences from FTB Ultimate
- Updated BuildCraft to 3.4.5
  - The Builder is disabled by default, as in 3.4.3 and 3.4.4, but can be enabled in the BuildCraft config (use caution)
  - Clay pipes
  - Assorted fixes, especially to the Filler
- Added Ears
  - This includes a backport of modern skin features and a skin fix
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
- Removed VoxelBox mods due to licensing issues
  - VoxelMenu is being rewritten from scratch in UpsilonFixes (not done yet)
  - VoxelPlayer has no replacement
  - VoxelMap can still be optionally used as it's a separate thing
- Removed LiteLoader, as it was only used by the VoxelBox mods
  - It will be reinstalled via NiteLoader if VoxelMap is installed

All of the following are done by UpsilonFixes, and can be disabled in its config:
- **Fixed water whirlpools (backported 1.5 water fill behavior) ([MC-916](https://bugs.mojang.com/browse/MC-916))**
- **PortalGun sounds fixed**
- **Fixed EE3 Minium stone recipes being broken after using them once or after NEI recipe lookup**
- **Items can be dragged over slots to spread them out (1.5 backport)**
- **Re-enabled SHA-1 jar signing to fix mods like Railcraft on latest Java 8 versions**
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
- MFFS update check removed
- GregTech capes removed as they contact broken Dropbox links
- Steve's Carts capes removed for the same reason
- Fixed MiscPeripherals ASM API misuse
- Fixed a CodeChickenCore transformer bug (only really visible alongside NilLoader)
- Patched ObjectWeb ASM to not explode on Java 8 classes

## Included Mods

- (Core) [CodeChickenCore](https://www.curseforge.com/minecraft/mc-mods/codechickencore) by Chicken_Bones
- (Core) [Ears](https://modrinth.com/mod/ears) by unascribed
- (Core) [FallingFix](https://www.curseforge.com/minecraft/mc-mods/fallingfix) by FyberOptic
- (Core) [MiscPeripherals](https://www.computercraft.info/forums2/index.php?/topic/4587-cc153mc152-miscperipherals-33/) by RichardG867
- (Core) [NilInjector](https://git.sleeping.town/unascribed/NilInjector) by unascribed
- (Core) [NotEnoughItems](https://www.curseforge.com/minecraft/mc-mods/notenoughitems) by Chicken_Bones
- (Core) [PowerCrystalsCore](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292152-powercrystals-mods-minefactoryreloaded) by PowerCrystals
- (Core) [RPTweaks](https://pastehtml.com/view/cr72r0hhu.html) by an anonymous author
- (Core) [SplashAnimation](https://www.curseforge.com/minecraft/mc-mods/splashanimation) by asiekierka (ported by unascribed)
- (Core) [VanillaNEIFix](https://www.curseforge.com/minecraft/mc-mods/vanilla-nei-fix) by FyberOptic
- [Advanced Machines](https://forum.industrial-craft.net/thread/4907-ic2-exp-1-7-10-advanced-machines-1-1-6/) by AtomicStryker
- [Advanced Solar Panel](https://forum.industrial-craft.net/thread/3291-ic2-exp-1-7-10-advanced-solar-panels-v3-5-1-quantum-generator-solar-helmets/) by SeNtiMeL
- [Applied Energistics](https://appliedenergistics.github.io/ae1-site-archive/) by AlgorithmX2
- [Auto Third Person](https://modrinth.com/mod/auto-third-person) by quaternary
- [BiblioCraft](https://www.curseforge.com/minecraft/mc-mods/bibliocraft/) by Nuchaz
- [Block Helper](https://modrinth.com/mod/block-helper) by HyperSpeeed
- [BuildCraft](https://mod-buildcraft.com/) by many people
- [ChargePads](https://www.curseforge.com/minecraft/mc-mods/chargepads) by Myrathi
- [ChickenChunks](https://www.curseforge.com/minecraft/mc-mods/chickenchunks) by Chicken_Bones
- [Chisel Retro](https://www.curseforge.com/minecraft/mc-mods/chisel-retro) by FyberOptic (a [custom fork](https://git.sleeping.town/unascribed/ChiselRetro/))
- [CoFHCore](https://www.curseforge.com/minecraft/mc-mods/cofh-core) by CoFH
- [ComputerCraft](https://www.computercraft.info/) by dan200
- [DartCraft](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1287878-dartcraft-beta-0-2-20) by bluedart
- [EE3](https://github.com/pahimar/Equivalent-Exchange-3) by Pahimar
- [Ender Storage](https://www.curseforge.com/minecraft/mc-mods/ender-storage) by Chicken_Bones
- [ExtraBees](https://web.archive.org/web/20180115013205/http://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1284348-1-7-10-1-6-4-forestry-binnies-mods-1-8-0-2-0-dev) by Binnie
- [ExtraBiomesXL](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1282126-extrabiomesxl-universal-3-16-3-for-mc-1-7-10) by many people
- [Factorization](https://modrinth.com/mod/factorization) by neptunepink
- [Flamingo](https://github.com/asiekierka/Flamingo) by copygirl (ported by asiekierka)
- [Forestry](https://modrinth.com/mod/forestry) by SirSengir
- [GraviSuite](https://forum.industrial-craft.net/thread/6915-ic2-exp-1-7-10-gravitation-suite-v2-0-3/) by SeNtiMeL
- [Gravity Gun](https://ichun.me/mods/gravity-gun/) by iChun
- [GregTech](https://gregtech.mechaenetia.com/downloads/gregtech_1.4.6/index.html) by GregoriusT
- [IC2](https://wiki.industrial-craft.net/index.php?title=Main_Page) by the IC² Dev Team
- [IC2 Nuclear Control](https://forum.industrial-craft.net/thread/5915-addon-v1-118-ssp-smp-nuclear-control-v-1-6-2b-e/) by Shedar
- [ImmibisCore](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1281065-immibiss-mods-now-with-85-7-less-version-numbers) by immibis
- [InvTweaks](https://www.curseforge.com/minecraft/mc-mods/inventory-tweaks) by Kobata
- [IronChests](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1280827-1-5-and-up-forge-universal-ironchests-5-0) by cpw
- [LegacyCustomPublish](https://modrinth.com/mod/legacycustompublish) by unascribed
- [LogisticsPipes](https://github.com/RS485/LogisticsPipes) by RS485
- [MineFactory Reloaded](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292152-powercrystals-mods-minefactoryreloaded) by PowerCrystals
- [Modular Force Field System](https://web.archive.org/web/20130114211225/http://forum.industrial-craft.net/index.php?page=Thread&threadID=1292) by Thunderdark
- [Modular Powersuits](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/wip-mods/1442976-machinemuses-modular-powersuits-finally-updated) by MachineMuse
- [Mystcraft](https://www.curseforge.com/minecraft/mc-mods/mystcraft) by XCompWiz
- [NEIPlugins](https://bitbucket.org/mistaqur/nei_plugins/wiki/Home) by mistaqur
- [NEIPluginsRedPower](https://www.curseforge.com/minecraft/mc-mods/nei-redpower-plugin) by Chicken_Bones
- [NetherOres](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292152-powercrystals-mods-minefactoryreloaded) by PowerCrystals
- [ObsidiPlates](https://www.curseforge.com/minecraft/mc-mods/obsidiplates) by Myrathi
- [OmniTools](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1284839-1-4-7-smp-omnitools-3-0-2-one-wrench-to-rule-them) by KingLemming
- [PetroGen](https://forum.feed-the-beast.com/threads/petroleum-generator-a-forestry-esque-bc-ic-crossover-mod.2246/) by DrCeph
- [PortalGun](https://ichun.me/mods/portalgun/) by iChun
- [PowerConverters](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292152-powercrystals-mods-minefactoryreloaded) by PowerCrystals (disabled by default)
- [Railcraft](https://www.curseforge.com/minecraft/mc-mods/railcraft) by Covert_Jaguar
- [RedPower2](http://www.eloraam.com/) by Eloraam
- [Rei's Minimap](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1275219-jul-08-reis-minimap-v3-4_01) by ReiFNSK
- [SecretRoomsMod](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1276042-v4-7-1-beta-secretroomsmod-malsis-doors-compat) by AbrarSyed
- [Soul Shards](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1285901-1-6-4-forgeirc-v1-0-18-soul-shards-v2-0-15-and) by ShadwDrgn
- [StevesCarts](https://web.archive.org/web/20150215153757/http://minecraftforum.net/forums/mapping-and-modding/minecraft-mods/1277433-1-6-steves-carts-2-v2-0-0-a123) by vswe
- [Thaumcraft](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1287022-thaumcraft-3-0-5i-outdated) by Azanor
- [ThaumicBees](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1287405-magic-bees-magic-themed-bees-for-forestry-the) by MysteriousAges
- [Thermal Expansion](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1288612-1-6-4-team-cofh-mods-thermal-expansion-3-0-0-0) by CoFH
- [Twilight Forest](https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest) by Benimatic
- [TubeStuff](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1281065-immibiss-mods-now-with-85-7-less-version-numbers) by immibis
- [WR-CBE](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1279956-chickenbones-mods) by Chicken_Bones
- [Xeno's Reliquary](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1287110-xenos-reliquary-v1-0-6d) by MercuriusXeno
- [XyCraft](https://web.archive.org/web/20140216215105/http://xycraft.wikispaces.com/) by Soaryn
- (Nil) [UpsilonFixes](https://git.sleeping.town/unascribed/UpsilonFixes) by unascribed
- (optional) UltimateSkyblock by emilyploszaj
- (optional) (Nil) [NiteLoader](https://git.sleeping.town/unascribed/NiteLoader) by unascribed
- (optional) [VoxelMap](https://www.curseforge.com/minecraft/mc-mods/voxelmap) by MamiyaOtaru
