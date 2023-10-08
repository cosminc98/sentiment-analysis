#!/bin/bash

source ./scripts/utils.sh
source ./scripts/constants.sh

if [ -d $VENV_PATH ]; then
    pexit "The virtual environment is already set up"
fi

function cleanup_venv () {
    rm -rf $VENV_PATH
}

which python3 > /dev/null || perr 1 "Python not installed"
python3 -m venv $VENV_PATH || (cleanup_venv; perr 2 "Could not create the virtual environment")

source $VENV_PATH/bin/activate || (cleanup_venv; perr 3)
pip install .[testing] || (cleanup_venv; perr 4)
