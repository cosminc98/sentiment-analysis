#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

bash ./scripts/setup_venv.sh || perr 1 "Could not set up the virtual environment"
source $VENV_PATH/bin/activate || perr 2

pytest
