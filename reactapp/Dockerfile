FROM node:16.13.0-alpine as builder

WORKDIR /app

COPY package.json /app

RUN npm install

CMD ["npm", "start"]