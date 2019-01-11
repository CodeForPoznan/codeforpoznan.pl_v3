#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=api
flask db migrate
flask db upgrade
flask run
