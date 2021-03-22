FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /car_dealer

RUN chmod +x /car_dealer/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /car_dealer/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /car_dealer/requirements/dev.txt
