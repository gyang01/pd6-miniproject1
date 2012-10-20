#!usr/bin/python
from pymongo import Connection

con = Connection("mongo.stuycs.org")
db = con.admin
res = db.authenticate("ml7","ml7")
