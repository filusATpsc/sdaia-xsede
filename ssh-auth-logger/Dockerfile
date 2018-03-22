FROM ubuntu:16.04

MAINTAINER Alex Withers version: 0.1

RUN apt-get update && apt-get install -y golang git && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV GOPATH=/usr

RUN go get -u -v github.com/JustinAzoff/ssh-auth-logger

EXPOSE 22

CMD ["/usr/bin/ssh-auth-logger"]

