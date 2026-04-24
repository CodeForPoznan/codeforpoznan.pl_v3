FROM node:18

WORKDIR /cfp_v3/frontend

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 8080

ENTRYPOINT ["bash", "docker-entrypoint.sh"]