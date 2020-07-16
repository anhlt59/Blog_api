FROM python:3.7-alpine
MAINTAINER AnhLT59.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache mysql mysql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN mkdir -p /static/media
RUN mkdir -p /static/skin
RUN adduser -D user
RUN chown -R user:user /static/
RUN chmod -R 755 /vol/blog
USER user
