#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

sudo docker run --rm -v $(pwd):/workdir -p $CONTAINER_PORT_MAPPING $DOCKER_IMAGE_NAME make start
