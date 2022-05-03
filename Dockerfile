FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install --no-install-recommends -y curl build-essential
RUN apt-get install -y gdal-bin libgdal-dev
ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal
RUN pip install gda-score-code

RUN pip3 install --upgrade pip

COPY ./photodel .
COPY ./requirments.txt .
RUN pip install -U Twisted[tls,http2]
ENV DJANGO_SETTINGS_MODULE=photodel.settings
RUN export DJANGO_SETTINGS_MODULE
RUN pip3 install -r ./requirments.txt
