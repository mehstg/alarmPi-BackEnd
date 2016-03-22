#!env/bin/python
import time, datetime, logging, sys
from dbConnector import dbConnector

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


db = dbConnector('alarmPi.db') 

#db.setEvent('reset')

records = db.getAllEvents()

print 'Printing whole records array:'
print records

output = []
for record in records:
    print 'Generating output dictionary'
    dt = time.strftime("%d-%m-%Y", time.gmtime(record[1]))
    tm = time.strftime("%H:%M:%S", time.gmtime(record[1]))
    output.append({u'Date': dt,  u'Time': tm, u'StateChange': record[2]})

print 'print output dictionary'

print output



db.setState('arm')

print 'Outputting state'
print db.getState()
