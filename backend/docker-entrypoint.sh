#!/bin/bash

wait-for-it "${DB_HOST}:${DB_PORT:-5432}"
flask db migrate
flask db upgrade
flask run --host=0.0.0.0
