#!/bin/bash -ex
(
	cd lang
	git pull
)
sed '/>8 cut here/q' .packwizignore |sponge .packwizignore
ag -l '^\{\}$' lang/ |sort >> .packwizignore
packwiz refresh
find -name '*.pw.toml' | zip -X -0 -@ unsup-metafiles.zip
brotli -Zjf unsup-metafiles.zip
keesign rewind pack.toml unsup.sig
