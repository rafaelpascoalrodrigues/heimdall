import mysql.connector
from mysql.connector import errorcode

import subprocess
import threading
import time

class Exec(threading.Thread):

	def __init__(self, threadId, serviceId, commandName):

		#PATH = '/usr/lib/heimdall/plugins/'
		self.PATH = 'monitors/'

		threading.Thread.__init__(self)
		self.command = self.PATH + commandName
		self.threadId = threadId
		self.serviceId = serviceId

	def run(self):
		output = subprocess.check_output(self.command, stderr=subprocess.STDOUT)
		print str(self.threadId) + ' : ' + output

		dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', 'localhost')
		dbHelper.connect2DB()

		query = ("INSERT INTO data (" 
		    " service_id,"
		    " run_date," 
		    " run_time,"
		    " data)"
		    " VALUES ("
		    + str(self.serviceId) + ","
		    " CURDATE(),"
		    " CURTIME(),"
		    "'" + output + "');")

		dbHelper.query(query)
		dbHelper.close()

class DBUtils():

	def __init__(self, user, password, database, host):
		self.conn = 'Null'
		self.user = user
		self.password = password
		self.database = database
		self.host = host
		
	def connect2DB(self):
		try:
			self.conn = mysql.connector.connect(user = self.user,
			                                    password = self.password,
			                                    database = self.database,
			                                    host = self.host)
		except mysql.connector.Error as e:
			print e

	def close(self):
		self.conn.close()

	def query(self, queryText):

		cursor = self.conn.cursor()

		try:
			cursor.execute(queryText)
		except mysql.connector.Error as e:
			return

		# Check if query returned something, if not commit the changes
		if cursor.rowcount >= 0:
			self.conn.commit()
			return
		return cursor.fetchall()