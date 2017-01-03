import lib.py
import database.py

dbHelper = DBUtils('heimdall', 'heimdall', 'heimdall', '127.0.0.1')
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



