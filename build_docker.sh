#!/bin/bash

docker build -t pylone .

docker run pylone

docker run --name pylone --rm -i -t pylone '/bin/sh'