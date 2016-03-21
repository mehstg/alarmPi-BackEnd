FROM debian:latest

RUN apt-get update
RUN apt-get install -y python python-pip wget
RUN pip install Flask

RUN mkdir /opt/alarmPi
COPY . /opt/alarmPi

WORKDIR /opt/alarmPi
ENTRYPOINT python flaskServer.py
