# Elemental Electronics

Elemental electronics is a game focused on realistic electrical engineering.
Where the users needs to improve their designs to gather resources.

## Project Implicit Dependencies

Its assumed that your system have the following packages installed

```
Python3
Docker
```

## First time

```
docker build -t debian:buster-ada -f DockerFile build/docker
git submodule update --init --recursive
```

## Building

The build the world simple run

```
python3 bake.py world
```

This will download and build all external dependencies and build the game world, unit tests etc.

##
