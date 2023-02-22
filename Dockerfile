# FROM python:3.9
# ADD . /app
# WORKDIR /app
# CMD [ "python3" ]

# Use existing docker image as a base
FROM alpine

# Download and install dependency
RUN apk update && apk upgrade && apk add python3

ADD . /app
WORKDIR /app
# EXPOSE the port to the Host OS
# EXPOSE 6379

# Tell the image what command it has to execute as it starts as a container
# CMD ["python3"]