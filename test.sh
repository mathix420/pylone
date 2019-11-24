#!/bin/bash

pip install . > /dev/null

OLD_PATH="$PWD"

mkdir -p "/tmp/pylone-test"

cd "/tmp/pylone-test"

pylone init

echo ;

tree

echo ;

cat config.yaml

echo ;

pylone init

cd "$OLD_PATH"

rm -rf "/tmp/pylone-test"
