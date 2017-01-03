import mysql.connector
from mysql.connector import errorcode

import subprocess
import threading
import time

class Exec(threading.Thread):

	PATH = '/usr/lib/heimdall/plugins/'

	def __init__(self, threadId, commandName):
		threading.Thread.__init__(self)
		self.command = PATH + commandName
		self.threadId = threadId

	def run(self):
		print self.command
		output = subprocess.check_output(self.command, stderr=subprocess.STOUT)
		print output

class DBUtils():

	def __init__(self, user, password, database, host):
		self.conn = Null
		self.connDescriptor = {'user':user,
		                        'password':password,
		                        'host':host,
		                        'database':database}

	def connect2DB():
		try:
			self.conn = mysql.connector.connect(self.connDescriptor)
		except mysql.connector.Error as e:
			print e

	def close():
		self.conn.close()

	def query(queryText):
		cursor = this.conn.cursor()
		try:
			cursor.execute(queryText)
		except mysql.connector.Error as e:
			print e
			return 0
		return cursor.fetchall()