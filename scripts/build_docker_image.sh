#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

# check dependencies
which docker > /dev/null || perr 1 "Docker not installed. Please install it first."

sudo docker build -t $DOCKER_IMAGE_NAME .devcontainer/ --no-cache
