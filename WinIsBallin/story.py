from pymongo import Connection

#Comm-link established
conn = Connection('mongo.stuycs.org')

#I am ADMIN
db = conn.admin
AUTHENTICATION = db.authenticate('ml7','ml7')

#Lets go period 6
db = conn['z-pd6']

#Our storybook <3
col = db["WinBall's StoryBook"]

def newStory(name):
    col.save({'name': name, 'lines': 0}) 

def newStoryStart(name, start):
    col.save({'name': name, 'lines': 0, 'text':start}) 

def continueStory(name, addition):
    col.update({'name':name}, {'$inc': {'lines':1}})
    col.update({'name':name}, {'$push': {'text':addition}})
    
def printStory(name):
    entries = col.find({'name':name},{'text':1})[0]['text']
    for entry in entries:
        print entry;

def getStoryNames():
    names = []
    for story in col.find():
        names.append(story['name'])
    return names
        
def getText(name):
    return col.find({'name':name},{'text':1})[0]['text']
    






if __name__ == "__main__":
    newStory("Hello World!")
    newStory("Story2")
    continueStory("Hello World!","hallo")
    continueStory("Story2", "There once was a man from australia")
    continueStory("Story2", "Whose limericks were quite a failure")
    
    test = 5

    for line in col.find():
        print line

    print

    for name in getStoryNames():
        print name

    print
    print

    printStory('Story2')

    col.drop()

