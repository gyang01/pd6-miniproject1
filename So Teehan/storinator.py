from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['SoTe-pd6']

def addstory(story):
    db.stories.save({story:['string']})

def addcontent(story, line):


addstory('the worst thing ever invented')
addstory('i dont know really')
addstory('arms and a man i sing')
