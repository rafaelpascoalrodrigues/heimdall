import mysql.connector
from mysql.connector import errorcode

import subprocess
import threading
import time

class Exec(threading.Thread):

	def __init__(self, threadId, commandName):

		#PATH = '/usr/lib/heimdall/plugins/'
		self.PATH = 'monitors/'

		threading.Thread.__init__(self)
		self.command = self.PATH + commandName
		self.threadId = threadId

	def run(self):
		output = subprocess.check_output(self.command, stderr=subprocess.STDOUT)
		print str(self.threadId) + ' : ' + output

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
			print e
			return
		# Check if query returned something
		if not cursor.rowcount:
			return
		return cursor.fetchall()