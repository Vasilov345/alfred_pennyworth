#!/usr/bin/env bash

./car_dealer/docker/scripts/wait-for-it.sh postgres:5432 -s -t 30 --

python car_dealer/src/manage.py runserver 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
