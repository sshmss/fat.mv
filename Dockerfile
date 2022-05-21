FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev zlib-dev jpeg-dev && \
    apk add postgresql-dev && \
    pip install -r requirements.txt && \
    apk del .build-deps

COPY . /code/