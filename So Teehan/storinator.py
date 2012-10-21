from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['SoTe-pd6']
storycontent = ''

def addstory(story):
    db.stories.save({story:['string']})

def addcontent(story, line):
    #collection.find_one({story})
    #db.stories.storycontent = db.stories.storycontent + '\n' +line

addstory('the worst thing ever invented')
addstory('i dont know really')
addstory('arms and a man i sing')
