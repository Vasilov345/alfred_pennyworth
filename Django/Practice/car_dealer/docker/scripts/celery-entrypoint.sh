#!/usr/bin/env bash

cd car_dealer && celery -A src.common.celery worker -l info --concurrency=2