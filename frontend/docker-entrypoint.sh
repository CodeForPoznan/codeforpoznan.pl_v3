#!/bin/bash

# https://github.com/docker/for-linux/issues/264
getent hosts host.docker.internal >/dev/null || \
    echo "$(ip route list match 0/0 | cut -d' ' -f3) host.docker.internal" \
    | tee -a /etc/hosts >/dev/null

yarn install
yarn serve --host 0.0.0.0
