#!env/bin/python
import sqlite3, os, time, logging

class dbConnector():
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
	logging.debug("Connecting to database")


    def setState(self, state):
	c = self.conn.cursor()
        logging.debug("SetState opening Sqlite cursor")

	#List of valid states - If state matches add record to db, otherwise fail.      
        availableStates = ['arm', 'disarm', 'triggered', 'reset']
	
	if state in availableStates:
		try:
                        output = c.execute('INSERT INTO Alarm_State(state) VALUES (?)', (state))
                        logging.info("Inserting in to sqlite database")
                except Exception as e:
                        logging.error("Error inserting in to SQLite database, rolling back")
                        self.conn.rollback()
                        raise e
			logging.error(e)	
                        return False

                finally:
                        self.conn.commit()
                        c.close()
                        logging.debug("Closing connection to SQLite database")
                        return True
        else:
		logging.error("State does not match list of available.")
                return False



    def getState(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM Alarm_State')
        logging.info("Selecting state records from SQLite database")
        data = c.fetchall()
        c.close()

        return data
	

    def setEvent(self, state):
	c = self.conn.cursor()
	logging.debug("SetEvent opening Sqlite cursor")

	#List of valid states - If state matches add record to db, otherwise fail.	
	availableStates = ['arm', 'disarm', 'triggered', 'reset']

	if state in availableStates:
		current_time = int(time.time())

		try:
			output = c.execute('INSERT INTO Alarm_Events(datetime,state) VALUES (?,?)', (current_time, state))
			logging.info("Inserting in to sqlite database")

		except Exception as e:
			logging.error("Error inserting in to SQLite database, rolling back")
			self.conn.rollback()
    			raise e
			return False

		finally:
			self.conn.commit()
			c.close()
			logging.debug("Closing connection to SQLite database")
			return True
	else:
			logging.error("State does not match list of available.")
			return False
	
    def getAllEvents(self):
	c = self.conn.cursor()
        c.execute('SELECT * FROM Alarm_Events')
	logging.info("Selecting event records from SQLite database")
        data = c.fetchall()
        c.close()

        return data

