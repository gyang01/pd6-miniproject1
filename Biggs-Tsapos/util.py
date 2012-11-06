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
    tmpline = tmpline + '<br/> <br/>' + line
    stories.update({'name':name},{'name':name,'lines':tmpline})

def getNumLines(name):
    tmp = stories.find_one({'name':name})['lines']
    return len(tmp)

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
    return tmpline

def numStories():
    count = 0
    tmp = stories.find()
    for line in tmp:
        count = count + 1
    return count

def getFirstLines():
    firstlines = []
    tmp = stories.find()
    for line in tmp:
        firstlines.append(line['name'])
    return firstlines

if __name__ == "__main__":
    #addStory('Hello my name is')
    #addLine('el oh el','hello')
    clearStories()
    #print getLines('Hello my name is')
    #showStories()
    #print getNumLines('hello')
