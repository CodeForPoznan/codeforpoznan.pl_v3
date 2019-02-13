FROM ubuntu:16.04

EXPOSE 5000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get install -y python3-pip libpq-dev && apt-get autoremove

RUN pip3 install --upgrade pip

ADD . /cfp_v3/backend
WORKDIR /cfp_v3/backend

RUN pip3 install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT bash docker-entrypoint.sh
