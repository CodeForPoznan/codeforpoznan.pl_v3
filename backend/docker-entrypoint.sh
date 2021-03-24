#!/bin/bash

# https://github.com/docker/for-linux/issues/264
getent hosts host.docker.internal >/dev/null || \
    echo "$(ip route list match 0/0 | cut -d' ' -f3) host.docker.internal" \
    | tee -a /etc/hosts >/dev/null

wait-for-it "${DB_HOST}:${DB_PORT}"
flask db migrate
flask db upgrade
flask run --host=0.0.0.0
