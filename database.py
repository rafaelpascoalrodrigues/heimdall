# Tables and databases especifications

DB = {}
DB['heimdall'] = 'heimdall'

TABLES = {}

TABLES['control_params'] = (
	"CREATE TABLE IF NOT EXISTS control_params ("
	"  param VARCHAR(50),"
	"  value VARCHAR(50),"
	"  PRIMARY KEY (param)"
	") ENGINE=InnoDB")

TABLES['services'] = (
	"CREATE TABLE IF NOT EXISTS services ("
	"  service_id int(11) NOT NULL AUTO_INCREMENT,"
	"  creation_date date,"
	"  creation_time time,"
	"  service_name VARCHAR(50),"
	"  service_args VARCHAR(50),"
	"  PRIMARY KEY (service_id)"
	") ENGINE=InnoDB")

TABLES['data'] = (
	"CREATE TABLE IF NOT EXISTS data ("
	"  service_id int(11),"
	"  run_date date,"
	"  run_time time,"
	"  data TEXT"
	") ENGINE=InnoDB")