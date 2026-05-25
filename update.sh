#!/bin/bash -ex
(
	cd lang
	git fetch origin trunk
	git reset --hard origin/trunk
	git push git@sleeping.town:Rewind/UpsilonLang.git release
)
sed '/>8 cut here/q' .packwizignore |sponge .packwizignore
rg -l '^\{\}$' lang/ |sort >> .packwizignore
packwiz refresh
find -name '*.pw.toml' | zip -X -0 -@ unsup-metafiles.zip
brotli -Zjf unsup-metafiles.zip
keesign rewind pack.toml unsup.sig
