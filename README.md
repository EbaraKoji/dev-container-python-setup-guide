# Dev Container with python

[VSCode: Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

[Dev Containers: Market Place](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setup

### Build Docker Image
```sh-sesseion
$ docker-compose -f .devcontainer/docker-compose.yml build
```

### Start Dev Container
View => Command Pallete => Dev Containers: Rebuild Container


### Format Python files
After starting dev containers, press `command + S` to format and `command + option + U` to unify quotes.
