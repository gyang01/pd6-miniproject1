from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

db = Connection.admin
res = db.authenticate('ml7', 'ml7')

db = Connection['z-pd6']

#Functions needed:
#-Get the stories list
#-Process story request and retrieve appropriate story
#-Add new line to current story
#-Make new story

def getStories() :
    """
    Returns the names of all the stories.
    """
    stories = db.mack.find()
    s = []
    for story in stories:
        s.append(story['name'])
    return s

def getStory(name) :
    """
    Returns the lines of the story with name name, if possible.
    """
    story = db.mack.find_one({'name': name})
    if(story) :
        return story['lines']
    else:
        return 'This story does not exist. How are you even seeing this?'

def addLine(story, l) :
    """
    Adds a line l to the story story.
    """
    db.mack.update({'name': story}, {'$push': {'lines': l}})

def addStory(name) :
    """
    Adds a story with the name name to db as long as there isn't one with the
    same name there already.
    """
    if(not db.mack.find_one('name': name)) :
        return 'There is already a story with that name. Pick a different one.'
    else :
        db.mack.save({'name': name, 'lines': []})

def removeStory(name):
    # removes a specific story
    db.mack.remove({'name': name})

def removeAll():
    # removes everything
    db.mack.remove()

def clearStory(name):
    #deletes all lines in a story
    db.mack.update({'name': name}, {'$set': {'lines': []}})  

def removeLastLine(name):
    #removes the last line in the story
     story = db.mack.find_one({'name': name})
     lines = []
    if(story) :
        lines =  story['lines']
    lines.pop()
    db.mack.update({'name': name), {'$set': {'lines': lines}})

def removeLine(name, index):
    # removes line at index
     story = db.mack.find_one({'name': name})
     lines = []
    if(story) :
        lines =  story['lines']
    lines.pop(index)
    db.mack.update({'name': name), {'$set': {'lines': lines}})    

def addLineAt(name, line, index):
    #adds a line at index
     story = db.mack.find_one({'name': name})
     lines = []
    if(story) :
        lines =  story['lines']
    lines.insert(index, line)
    db.mack.update({'name': name), {'$set': {'lines': lines}}) 
