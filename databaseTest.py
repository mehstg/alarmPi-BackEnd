#!env/bin/python
from dbConnector import dbConnector

db = dbConnector('alarmPi.db') 

db.setRecord('reset')

records = db.getAllRecords()

print 'Printing whole records array:'
print records

output = []
for record in records:
    print 'Generating output dictionary'
    output.append({u'epoch': record[1], u'StateChange': record[2]})

print 'print output dictionary'

print output
