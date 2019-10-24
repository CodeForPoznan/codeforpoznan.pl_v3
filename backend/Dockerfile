FROM python:3.8

EXPOSE 5000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get install -y libpq-dev && apt-get autoremove

RUN pip install --upgrade pip
RUN apt-get update

# update pip
RUN python -m pip install pip --upgrade

ADD . /cfp_v3/backend
WORKDIR /cfp_v3/backend

RUN pip install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT bash docker-entrypoint.sh
