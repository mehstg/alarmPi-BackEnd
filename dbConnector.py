#!/usr/local/bin/python
import sqlite3, os, time


class dbConnector(dbName):
    def __init__(self, region):
        conn = sqlite3.connect(dbName)
        c = conn.cursor()

    def setRecord():
	current_time = int(time.time())

	insert = (current_time, 'Arm'),

	try:
    		with c:
			c.execute('INSERT INTO Alarm_Events(datetime,state) VALUES (?,?)', insert)
			return True
	except sqlite3.IntegrityError:
		return False


    def getRecord():




    def getAllRecords():
