from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

def beg():
db = Connection.admin
res= db.authenticate('ml7','ml7')
db = Connection['Amanda-Emily-pd6']
collection = db[test_collection]

def addstory(prompt):
db = Connection['Amanda-Emily-pd6']
collection = db[test_collection]
collection.insert( {'name': prompt, 'line': 0 } ) #not sure if this is right!


