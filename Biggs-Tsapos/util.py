from pymongo import Connection

Conn = Connection('mongo.stuycs.org')

db = Conn.admin
res = db.authenticate('ml7','ml7')
db = Conn['pd6-bigzam']
stories = db.stories

def addStory(name):
    stories.insert({'name':name,'lines':''})

def addLine(line,name):
    tmpline = stories.find_one({'name':name})['lines']
    tmpline = tmpline + '\n' + line
    stories.update({'name':name},{'name':name,'lines':tmpline})

def showStories():
    tmp = stories.find()
    for lines in tmp:
        print(lines)

def clearStories():
    tmp = stories.find()
    for lines in tmp:
        stories.remove(lines)

def getLines(name):
    tmpline = stories.find_one({'name':name})['lines']
    return str(tmpline)

#addStory('Hello my name is')
#addLine('el oh el','Hello my name is')
#clearStories()
#print getLines('Hello my name is')
#showStories()
