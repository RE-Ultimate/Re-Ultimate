#!/bin/bash -ex
packwiz refresh
find -name '*.pw.toml' | zip -X -0 -@ unsup-metafiles.zip
brotli -Zjf unsup-metafiles.zip
keesign rewind pack.toml unsup.sig
