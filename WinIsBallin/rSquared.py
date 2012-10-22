from pymongo import Connection

#Comm-link established
conn = Connection('mongo.stuycs.org')

#I am ADMIN
db = conn.admin
AUTHENTICAAAATion = db.authenticate('ml7','ml7')

#Lets go period 6
db = conn['z-pd6']

#Our storybook <3
col = db["WinBall's StoryBook"]

def newStory(name):
    col.save({'name': name, 'lines': 0}) 

newStory("Hello World!")
test = 5

for line in col.find():
    print line

col.drop()
