from lib import *
from database import *

from math import ceil

dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', 'localhost')
dbHelper.connect2DB()

# Create tables in db
dbHelper.query(TABLES['control_params'])
dbHelper.query(TABLES['services'])
dbHelper.query(TABLES['data'])

"""

# Must figure out how to effectively run 'max_concurrent_services' per time

# Initialize control_params with max_concurrent_services
dbHelper.query("INSERT INTO control_params (param, value) VALUES ('max_concurrent_services', '50');")

# Check how many services are there to run
maxConcurrentServices = dbHelper.query("SELECT value FROM control_params WHERE param LIKE 'max_concurrent_services';")
services_num = dbHelper.query('SELECT COUNT(*) FROM services')

timesToRun = ceil(services_num[0][0] / maxConcurrentServices[0][0])

"""

# Select from DB programs to run
services = dbHelper.query('SELECT service_id, service_name, service_args FROM services;')

# Create and execute services as threads
threadId = 0

for (service_id, service_name, service_args) in services:
	if not service_args:
		command = service_name
	else:
		command = service_name + ' ' + service_args

	t = Exec(threadId, service_id, command)
	t.start()

	threadId += 1

dbHelper.close()



