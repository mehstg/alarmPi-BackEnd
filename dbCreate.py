#!env/bin/python

#Build SQLite table for alarm logging

import sqlite3, os
database = 'alarmPi.db'


conn = sqlite3.connect(database)
c = conn.cursor()

c.execute("CREATE TABLE Alarm_Events(id integer primary key, datetime integer, state text)")
c.execute("CREATE TABLE Alarm_State(id integer primary key, currentstate text)")

