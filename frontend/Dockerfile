FROM node:18

EXPOSE 8080

WORKDIR /cfp_v3/frontend

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

ENTRYPOINT ["bash", "docker-entrypoint.sh"]