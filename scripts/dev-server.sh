#!/bin/sh
set -e
python finance/manage.py makemigrations --no-input
python finance/manage.py migrate --no-input
python finance/manage.py runserver 0.0.0.0:8000
