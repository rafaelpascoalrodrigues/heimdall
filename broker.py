# Coded bt DTil 29/12/2016

import threading
import time

import mysql.connector
from mysql.connector import errorcode


class DBBroker():
	def __init__(self, user, password, database, host):
		self.conn = Null
		self.connDescription = {'user':user,
								'password':'password',
								'host':host,
								'database':database}

	def connect2DB():
		try:
			self.conn = mysql.connector.connect(self.connDescript)
		except mysql.connector.Error as e:
			print e

	def close():
		self.conn.close()

	def query():
		# To do...

class Broker(threading.Thread):
	def __init__(self, threadId, threadName):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.threadName = threadName
	def run(self):
		#execute()

		# To do...

