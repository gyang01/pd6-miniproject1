from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
global connection, db, res, collection
def beg():
  db = Connection.admin
  res= db.authenticate('ml7','ml7')
  db = Connection['AmandaEmily']
  collection = db['stories']

def addstory(name):
  global collection
  db = Connection['AmandaEmily']
  collection.insert( {'name': name, 'body':[] } ) 
  

def getStory(title):
  Storytext = []
  res = collection.find()
  for x in res:
    if (str(x['name'])) == title:
      Storytext.append(str(x['body']))
  print Storytext
  

def getAllTitles():
  allTitles= []
  res = collection.find()
  for x in res:
    allTitles.append(str(x['name']))
  print allTitles

def addLine(name, line):
  global collection
  res = collection.find_one({'name':name})
  if res:
    newlines=res['body']
    newlines.append(line)
    collection.update({'name':name},{'name':name, 'body':[newlines]}) 
if __name__ == "__main__":
  beg()
  db = Connection['AmandaEmily']
  collection = db['stories']
  addstory('There was once a sad puppy named Biscuit')
  addLine('There was once a sad puppy named Biscuit', 'who loved to read')
  getStory('There was once a sad puppy named Biscuit')
  addstory('Once upon a time there was')
  print getAllTitles()
  collection.drop()
