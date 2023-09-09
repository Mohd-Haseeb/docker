FROM node:17.9.0 as node

WORKDIR /app

COPY package.json /app

RUN npm install

COPY .  /app

EXPOSE 80

CMD [ "node", "server.js" ]