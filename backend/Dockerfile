FROM ubuntu:18.04
FROM python:3.8

EXPOSE 5000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get install -y libpq-dev && apt-get autoremove

RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get install -y git

# update pip
RUN python3.8 -m pip install pip --upgrade
RUN python3.8 -m pip install wheel


ADD . /cfp_v3/backend
WORKDIR /cfp_v3/backend

RUN pip3.8 install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT bash docker-entrypoint.sh
