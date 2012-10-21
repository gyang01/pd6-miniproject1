from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

def beg():
db = Connection.admin
res= db.authenticate('ml7','ml7')
db = Connection['Amanda-Emily-pd6']
collection = db['stories']

def addstory(name):
db = Connection['Amanda-Emily-pd6']
collection = db['stories']

collection.insert( {'name': name, body: 'body' } ) 

def getStory(title):
db = Connection['Amanda-Emily-pd6]
collection = db['stories']
Storytext[]
res = collection.find()
  for x in res:
    if (str(x['name'])) == title
      Storytext.append(x)
print Storytext
  

def getAllTitles():
db = Connection['Amanda-Emily-pd6]
collection = db['stories']
allTitles[]
res = collection.find()
for x in res:
  allTitles.append(str(x['name']))
print allTitles

#def addLine()
