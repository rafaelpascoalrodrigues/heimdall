# Coded bt DTil 29/12/2016

import threading
import mysql.connector
import time

class DBBroker():
	def __init__(self, user, password, database, host):
		self.conn = Null
		self.connDescription = {'user':user,
								'password':'password',
								'host':host,
								'database':database}
	def connect2DB():
		self.conn = mysql.connector.connect(self.connDescript)
	def close():
		self.conn.close()
	

class Broker(threading.Thread):
	def __init__(self, threadId, threadName):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.threadName = threadName
	def run(self):
		execute()

