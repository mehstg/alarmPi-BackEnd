#!env/bin/python
import time, datetime, logging, sys
from dbConnector import dbConnector

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


db = dbConnector('alarmPi.db') 

db.setEvent('disarm')

records = db.getAllEvents()


output = []
for record in records:
    dt = time.strftime("%d-%m-%Y", time.gmtime(record[1]))
    tm = time.strftime("%H:%M:%S", time.gmtime(record[1]))
    output.append({u'Date': dt,  u'Time': tm, u'StateChange': record[2]})





db.setState('arm')

print db.getState()
