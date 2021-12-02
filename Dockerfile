FROM python:3.8-slim


WORKDIR /code

COPY requirements.txt /code/

RUN set -ex && \
    pip3 install -r requirements.txt

COPY . /code/
