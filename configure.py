#!/usr/bin/python

from database import *
from lib import *

import os

def buildDB():

	dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', 'localhost')
	dbHelper.connect2DB()

	# Create tables in db
	dbHelper.query(TABLES['control_params'])
	dbHelper.query(TABLES['services'])
	dbHelper.query(TABLES['data'])

	# Insert services in DB
	PATH = 'monitors/'
	
	for service in os.listdir(PATH):
		query = ("INSERT INTO services ("
            " service_id,"
            " creation_date," 
            " creation_time,"
            " service_name,"
            " service_args)"
            " VALUES ("
            " '',"
            " CURDATE(),"
            " CURTIME(),"
            "'" + service + "',"
            "'');")

		dbHelper.query(query)

	dbHelper.close()


# Configure DB
buildDB()