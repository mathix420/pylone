<img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/223/tokyo-tower_1f5fc.png" width="100" height="100" align="right" alt="Pylone icon">

# PYLONE

**Python CD framework**

[![Pypi](https://badgen.net/pypi/v/pylone)](https://pypi.org/project/pylone/)
[![Docker Pulls](https://badgen.net/docker/pulls/plsr/pylone?icon=docker&label=pulls)](https://hub.docker.com/r/plsr/pylone/)

[![wakatime](https://wakatime.com/badge/github/mathix420/pylone.svg)](https://wakatime.com/badge/github/mathix420/pylone)
[![Maintainability](https://api.codeclimate.com/v1/badges/fc078176e896556db324/maintainability)](https://codeclimate.com/github/mathix420/pylone/maintainability)

# Usage

## Pylone usage

```bash
pylone -h
```

# Template reference

## `stages` global parameter

You can set the `stages` parameter to have a multistage project
```yaml
stages:
    - dev # first one is used as default stage
    - prod # all other stages are more advanced stages
```

## `source` parameter

You can use the `source` parameter to force a directory to be used as source
```yaml
source: ./bin
```

## `before-script` parameter

You can use the `before-script` parameter to execute a bash script before processing an entity
```yaml
before-script: ./script.sh
# OR
before-script: "echo 'Starting ...'"
```

## `after-script` parameter

Similar as `before-script` but launch script at the end of process
```yaml
after-script: ./script.sh
# OR
after-script: "echo 'END of process'"
```

## `bucket-name` parameter

> Default value: `pylone-bucket`

Allows you to choose the bucket name where pylone will upload zip files.
```yaml
bucket-name: tmp-pylone-files
```
