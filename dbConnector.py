#!/usr/local/bin/python
import sqlite3, os, time

class dbConnector():
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)

    def setRecord(self):
	c = self.conn.cursor()

	current_time = int(time.time())
	insert = [(current_time, 'Arm'),]

	try:
		output = c.execute('INSERT INTO Alarm_Events(datetime,state) VALUES (?,?)', (current_time, 'Arm'))

	except Exception as e:
		self.conn.rollback()
    		raise e
		return False

	finally:
		self.conn.commit()
		c.close()
		return True
	

    def getRecords(self):
	c = self.conn.cursor()
	c.execute('SELECT * FROM Alarm_Events')
	data = c.fetchall()
	c.close()

	return data




    def getAllRecords(self):
	return true
