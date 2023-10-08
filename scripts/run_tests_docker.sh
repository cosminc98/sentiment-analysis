#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

sudo docker run --rm $DOCKER_IMAGE_NAME make test
