from database_manager import DatabaseManager
import log_lib
import sys

SQLALCHEMY_DATABASE_URI = "mysql://lus:lus@password@localhost:3306/lus"

dbm = DatabaseManager(SQLALCHEMY_DATABASE_URI)
