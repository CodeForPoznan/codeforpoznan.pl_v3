#!/bin/bash

python3 manage.py db migrate
python3 manage.py db upgrade
python3 app.py
