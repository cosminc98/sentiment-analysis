#!/bin/bash

function perr () {
    echo "ERROR: $2"
    exit $1
}

function pexit () {
    echo $1
    exit 0
}
