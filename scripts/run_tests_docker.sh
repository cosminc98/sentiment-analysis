#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

sudo docker run --rm -v $(pwd):/workdir $DOCKER_IMAGE_NAME make test
