FROM ubuntu:20.04

WORKDIR /app

COPY . .

RUN apt-get update 
RUN apt-get install python3-pip -y
RUN pip3 install fastapi pymongo uvicorn 


