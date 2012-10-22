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
  collection.insert( {'name': name, 'body': [name] } ) 
  

def getStory(title):
  Storytext = []
  res = collection.find()
  for x in res:
    if (str(x['name'])) == title:
      Storytext.append(x)
  print Storytext
  

def getAllTitles():
  allTitles= []
  res = collection.find()
  for x in res:
    allTitles.append(str(x['name']))
  print allTitles

def addLine(title, line):
  global collection
  res = collection.find_one({'name': title})
  if res:
    newlines=res['body']
    newlines.append(line)
    collection.update({'name': name},{'name': name, 'body':[newlines]}) #not sure about this
if __name__ == "__main__":
  beg()
  db = Connection['AmandaEmily']
  collection = db['stories']
  addstory('There was once a sad puppy named Biscuit')
  #addLine('There was once a sad puppy named Biscuit', 'who loved to read')
  getStory('There was once a sad puppy named Biscuit')
  addstory('Once upon a time there was')
  print getAllTitles()
  collection.drop()
