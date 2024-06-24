###########
# STAGE 1 #
###########

FROM node:18-alpine as builder

# set working directory
WORKDIR /app

# install app dependencies
COPY ./ .
RUN npm install

# build
RUN npm run build

###########
# STAGE 2 #
###########

FROM nginx:1.25.3

# set working directory
WORKDIR /etc/nginx

# Remove the default nginx configuration
RUN rm -f nginx.conf

# Copy your custom nginx configuration
COPY nginx.conf nginx.conf

# set working directory for the app
WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

# add app
COPY --from=builder /app/build/ .

# start app
CMD ["nginx", "-g", "daemon off;"]

