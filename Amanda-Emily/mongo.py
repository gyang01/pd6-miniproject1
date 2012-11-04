from pymongo import Connection

Connection = Connection('mongo.stuycs.org')
def beg():
  db = Connection.admin
  res= db.authenticate('ml7','ml7')
  db = Connection['AmandaEmily']
  collection = db['stories']
  return collection

def addstory(name):
  collection = beg()
  if(collection.find({'name': name}).count() == 0):
    collection.insert( {'name': name, 'body':[] } )
  else:
    return False
  

def getStory(name):
  collection = beg()
  for x in collection.find({'name': name }):
    return x['body']

def getAllTitles():
  collection = beg()
  allTitles= []
  res = collection.find()
  for x in res:
    allTitles.append(str(x['name']))
  print allTitles

def addLine(name, line):
  collection = beg()
  res = collection.find_one({'name':name})
  if res:
    newlines=res['body']
    newlines.append(line)
    collection.update({'name':name},{'name':name, 'body':[newlines]}) 
if __name__ == "__main__":
  collection = beg()
  collection.drop()
 
