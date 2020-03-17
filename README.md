<p align="center"><img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/223/tokyo-tower_1f5fc.png"></p><br/>
<h1 align="center">PYLONE</h1><br/>
<h3 align="center">Python CD framework</h3><br/>


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