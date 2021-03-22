FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /car_dealer

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /car_dealer/requirements/dev.txt

WORKDIR car_dealer/src