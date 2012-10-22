from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

db = Connection.admin
res=db.authenticate('ml7','ml7')

db = Connection['SofiaSarah']

collection = db['stories']

def addStory(title):
    collection.insert( {'title': title, 'lines': [title] } )

def getStory(title):
    stories = collection.find()
    for s in stories:
        if (str(s['title'])) == title:
            return s
