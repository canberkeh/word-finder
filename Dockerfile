# syntax=docker/dockerfile:1

FROM python:3.9.5

ADD . /WORD-FINDER
WORKDIR /WORD-FINDER
RUN pip install -r requirements.txt