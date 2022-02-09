FROM node:12

EXPOSE 8080

ADD . /cfp_v3/frontend
WORKDIR /cfp_v3/frontend

RUN yarn install

ENTRYPOINT bash docker-entrypoint.sh
