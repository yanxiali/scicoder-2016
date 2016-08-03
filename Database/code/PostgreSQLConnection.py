#!/usr/bin/python

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from scicoder.database.DatabaseConnection import DatabaseConnection

# ---------------------------------------------
# Fill in database connection information here.
# ---------------------------------------------
db_config = {
	'user'     : 'xxxx', # specify the database username
	'password' : 'xxxx',		 # the database password for that user
	'database' : 'xxxx', # the name of the database
	'host'     : 'xxxx.xxxx.edu', # your hostname, "localhost" if on your own machine
	'port'     : 5432
}

database_connection_string = 'postgresql://%s:%s@%s:%s/%s' % \
	(db_config["user"], db_config["password"], db_config["host"],\
	db_config["port"], db_config["database"])

# This allows the file to be 'import'ed any number of times, but attempts to
# connect to the database only once.
try:
	db = DatabaseConnection() # fails if connection not yet made.
except:
	db = DatabaseConnection(database_connection_string=database_connection_string)

engine = db.engine
metadata = db.metadata
Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))

