# pylone
Python serverless framework

# Usage

## Start a project

To start a new pylone project just type 
```
pylone init
```
## Create a function

```
pylone create-function
```

## Create a layer

```
pylone create-layer
```

## Push architecture

```
pylone push
```

# Template reference

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