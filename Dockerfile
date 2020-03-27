FROM python:3.7-alpine

COPY ./requirements.txt requirements.txt
COPY ./rest_project /rest_project

RUN apk update \
    && apk add \
      bash \
      build-base \
      curl \
      g++ \
      gcc \
      libxslt-dev \
      gettext \
      git \
      libffi-dev \
      linux-headers \
      postgresql-dev \
      tini \
      jpeg-dev \
      zlib-dev \
      openjpeg-dev && rm -vrf /var/cache/apk/*

RUN pip install -r /requirements.txt

WORKDIR /rest_project
RUN mkdir -p /web/media
RUN mkdir -p /web/static

RUN adduser -D user
RUN chown -R user:user /web
RUN chmod -R 755 /web

USER user