FROM python:3.7-alpine

COPY . /sctp
WORKDIR /sctp/

RUN apk add build-base lksctp-tools-dev lksctp-tools musl-dev linux-headers
RUN pip install pysctp 

EXPOSE 6000