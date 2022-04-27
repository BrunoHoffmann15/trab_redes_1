FROM python:3.7-alpine

COPY /src /udp-network
WORKDIR /udp-network/

EXPOSE 6000