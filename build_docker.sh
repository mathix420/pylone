#!/bin/bash

current_version=$(cat setup.py | grep version | awk -F "'" '{print $2}')

docker build -t "plsr/pylone:latest" -t "plsr/pylone:$current_version" .

# docker run plsr/pylone
# docker run --name plsr/pylone --rm -i -t plsr/pylone '/bin/sh'
