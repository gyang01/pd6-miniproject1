from pymongo import Connection

#Comm-link established
conn = Connection('mongo.stuycs.org')

#I am ADMIN
db = conn.admin
AUTHENTICAAAATion = db.authenticate('ml7','ml7')

#Lets go period 6
db = conn['z-pd6']

#Our storybook <3
col = db.WinBalls_StoryBook

def newStory():
    db.WinBalls_StoryBook.save({'name': 5}) 


test = 5

newStory()

print conn.cursor()
