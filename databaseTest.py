#!/usr/local/bin/python
from dbConnector import dbConnector

db = dbConnector('alarmPi.db') 

db.setRecord()

print db.getRecords()
