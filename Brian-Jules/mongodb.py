#!usr/bin/python
from mongo import Connection

class DatabaseConnection(object):
col

def __init__(self):
    self.db = self.get_db()

def get_db():
    connection = Connection("mongo.stuycs.org")
    admin = connection.admin
    admin.authenticate("ml7", "ml7")
    return connection["JulesBrian"]

def add_story(story):
    col = self.db["Stories"]
    col.append(story)

def get_story():
    pass

def add_line(line):
    pass
    



