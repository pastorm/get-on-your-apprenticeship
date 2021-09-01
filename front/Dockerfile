# BUILDER
FROM node:13.12.0-alpine as build

WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json package-lock.json /app/

RUN npm install
RUN npm install react-scripts@3.4.1 -g

COPY . /app/

RUN npm run build

# PROD
FROM nginx:stable-alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
