from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
global connection
global res
global db
global collection

def beg():
global connection
global res
global db
global collection
db = Connection.admin
res= db.authenticate('ml7','ml7')
db = Connection['Amanda-Emily-pd6']
collection = db['stories']

def addstory(name):
db = Connection['Amanda-Emily-pd6']
collection = db['stories']
if not name in getAllTitles():
  collection.insert( {'name': name, body: [name] } ) 
else:
#what to do here

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

def addLine(title, line):
res = collection.find_one({'name': title})
if res:
  newlines=res['lines']
  newlines.append(line)
  newlines.set({name: 'name'}{'$set': {'body':[newlines]}) #not sure about this method

