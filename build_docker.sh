#!/bin/bash

docker build -t plsr/pylone .

docker run plsr/pylone

docker run --name plsr/pylone --rm -i -t plsr/pylone '/bin/sh'