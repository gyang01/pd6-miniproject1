from pymongo import Connection

def startConnection() :
    connection = Connection('mongo.stuycs.org')
    
    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    
    db = connection['z-pd6']
    return db

#Functions needed:
#-Get the stories list
#-Process story request and retrieve appropriate story
#-Add new line to current story
#-Make new story

def getStories(db) :
    """
    Returns the names of all the stories.
    """
    stories = db.find()
    s = []
    for story in stories:
        s.append(str(story['name']))
    return s

def getStory(db, name) :
    """
    Returns the lines of the story with name name, if possible.
    """
    story = db.find_one({'name': name})
    if(story) :
        s = []
        for line in story['lines']:
            s.append(str(line))
        return s
    else:
        return 'This story does not exist. How are you even seeing this?'

def addLine(db, story, l) :
    """
    Adds a line l to the story story.
    """
    db.update({'name': story}, {'$push': {'lines': l}})

def addStory(db, name) :
    """
    Adds a story with the name name to db as long as there isn't one with the
    same name there already.
    """
    if(db.find_one({'name': name})) :
        return 'There is already a story with that name. Pick a different one.'
    else :
        db.save({'name': name, 'lines': []})

def removeStory(db, name):
    # removes a specific story
    db.remove({'name': name})

def removeAll(db):
    # removes everything
    db.remove()

def clearStory(db, name):
    #deletes all lines in a story
    db.update({'name': name}, {'$set': {'lines': []}})

def removeLastLine(db, name):
    #removes the last line in the story
    story = db.find_one({'name': name})
    lines = []
    if(story) :
        lines = story['lines']
    lines.pop()
    db.update({'name': name}, {'$set': {'lines': lines}})

def removeLine(db, name, index):
    # removes line at index
    story = db.find_one({'name': name})
    lines = []
    if(story) :
        lines = story['lines']
    lines.pop(index)
    db.update({'name': name}, {'$set': {'lines': lines}})

def addLineAt(db, name, line, index):
    #adds a line at index
    story = db.find_one({'name': name})
    lines = []
    if(story) :
        lines = story['lines']
    lines.insert(index, line)
    db.update({'name': name}, {'$set': {'lines': lines}})

#main method
if __name__ == '__main__' :
    db = startConnection()
    try:
        db.create_collection('mack')
    except:
        pass
    mack = db.mack
    storyname = 'The Tale of How Bad Development for SwordQuest 2 Was Going'
    addStory(mack, storyname)
    addLine(mack, storyname, 'Beginning of May')
    addLine(mack, storyname, 'This is going great, we\'ll totally finish!')
    addStory(mack, 'Goblins and Orcs Yay')
    print getStory(mack, storyname)
    print getStories(mack)
    clearStory(mack, storyname)
    removeAll(mack)
    print getStories(mack)
