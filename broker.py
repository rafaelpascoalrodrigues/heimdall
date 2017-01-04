from lib import *
from database import *

dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', 'localhost')
dbHelper.connect2DB()

# Create tables in db
dbHelper.query(TABLES['services'])
dbHelper.query(TABLES['data'])

# Select from DB programs to run
services = dbHelper.query('SELECT service_name, service_args FROM services;')

# Create and execute services as threads
threadId = 0

for (service_name, service_args) in services:
	if not service_args:
		t = Exec(threadId, service_name)
	else:
		t = Exec(threadId, service_name + ' ' + service_args)

	t.run()
	threadId += 1

# Record output to DB
  # Todo

dbHelper.close()



