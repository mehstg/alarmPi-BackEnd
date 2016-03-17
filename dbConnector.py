#!/usr/local/bin/python
import sqlite3, os, time

class dbConnector():
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)

    def setRecord(self, state):
	c = self.conn.cursor()

	#List of valid states - If state matches add record to db, otherwise fail.	
	availableStates = ['arm', 'disarm', 'triggered', 'reset']

	if state in availableStates:
		current_time = int(time.time())

		try:
			output = c.execute('INSERT INTO Alarm_Events(datetime,state) VALUES (?,?)', (current_time, state))

		except Exception as e:
			self.conn.rollback()
    			raise e
			return False

		finally:
			self.conn.commit()
			c.close()
			return True
	else:
		return False
	
    
    def getAllRecords(self):
	c = self.conn.cursor()
        c.execute('SELECT * FROM Alarm_Events')
        data = c.fetchall()
        c.close()

        return data

