#!env/bin/python
import sqlite3, os, time, logging

class dbConnector():
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName, check_same_thread = False)
	logging.debug("Connecting to database")

    availableStates = ['arm', 'disarm', 'triggered', 'reset']

    def setState(self, state):
	c = self.conn.cursor()
        logging.debug("SetState opening Sqlite cursor")

	#Delete rows in Alarm_State
	try:
		drop = c.execute('DELETE FROM Alarm_State')
		logging.debug("Deleting rows from Alarm_State")
	except Exception as d:
		logging.error("Unable to delete rows from Alarm_State")
		self.conn.rollback()
		raise d
		return False
	finally:
		self.conn.commit()
		c.close
		logging.debug("Successfully deleted rows from Alarm_State")
	
	
	if state in self.availableStates:
		try:
			output = c.execute('INSERT INTO Alarm_State(currentstate) VALUES (?)', (str(state),))
                	logging.info("Inserting in to Alarm_State table")
                
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


	if state in self.availableStates:
		current_time = int(time.time())

		try:
			output = c.execute('INSERT INTO Alarm_Events(datetime,state) VALUES (?,?)', (int(current_time), str(state)))
			logging.info("Inserting in to Alarm_Events table")

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
        c.execute('SELECT * FROM Alarm_Events ORDER BY datetime DESC')
	logging.info("Selecting event records from SQLite database")
        data = c.fetchall()
        c.close()

        return data

