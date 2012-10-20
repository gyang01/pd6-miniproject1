from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

def beg():
db = Connection.admin
res= db.authenticate('ml7','ml7')
db = Connection['Amanda-Emily-pd6']
collection = db['stuff']

def addstory(prompt):
db = Connection['Amanda-Emily-pd6']
collection = db['stuff']
collection.insert( {'name': prompt, 'line': [prompt] } ) #not sure if this is right!

def getStory(title):
db = Connection['Amanda-Emily-pd6]
collection = db['stuff']
selected = db.find( {'name': title } )
print selected

