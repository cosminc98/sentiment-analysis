FROM ubuntu:22.04

ARG WORK_DIR=$HOME/workdir

RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 python3-venv make \
  && rm -rf /var/lib/apt/lists/*

ADD pyproject.toml Makefile README.md $WORK_DIR/
ADD scripts/* $WORK_DIR/scripts/
ADD tests/*.py $WORK_DIR/tests/
ADD vaderapi/*.py $WORK_DIR/vaderapi/
ADD vaderapi/configs $WORK_DIR/vaderapi/configs

WORKDIR $WORK_DIR
