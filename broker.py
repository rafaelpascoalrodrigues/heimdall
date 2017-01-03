from lib import *
from database import *

dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', 'localhost')
dbHelper.connect2DB()

# Create tables in db
dbHelper.query(TABLES['services'])
dbHelper.query(TABLES['data'])

# Select from DB programs to run
  # Todo
# Create and execute plugins as threads
  # Todo
# Record to DB plugin output
  # Todo

dbHelper.close()



