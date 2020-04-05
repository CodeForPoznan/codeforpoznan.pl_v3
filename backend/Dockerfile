FROM python:3.8

EXPOSE 5000

RUN apt-get update -y && apt-get install -y libpq-dev wait-for-it && apt-get autoremove

# update pip
RUN pip install --upgrade pip

ADD . /cfp_v3/backend
WORKDIR /cfp_v3/backend

RUN pip install -r requirements.txt
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT bash docker-entrypoint.sh
