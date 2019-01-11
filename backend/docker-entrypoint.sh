#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=api
export FLASK_ENV=development
flask db migrate
flask db upgrade
flask run --host=0.0.0.0
