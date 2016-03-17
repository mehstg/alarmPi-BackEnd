#!/usr/local/bin/python
from dbConnector import dbConnector

db = dbConnector('alarmPi.db') 

print db.setRecord()
