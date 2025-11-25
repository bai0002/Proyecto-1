FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3.9 python3-pip
#FROM python:3.9
WORKDIR /pml0015
COPY . .
RUN pip3 install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8081 app:app  
