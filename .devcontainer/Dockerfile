FROM ubuntu:22.04

RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 python3-venv make curl git \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workdir
