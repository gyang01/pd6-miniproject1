from pymongo import Connection
global connection
global db
global res
global col

def auth():
    global connection
    global db
    global res
    global col
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    col = db['DLWS']

def addStory(title):
    global col
    col.insert({'title': title, 'lines':[title]})

def addLine(title, line):
    global col
    res = col.find_one({'title': title})
    if res:
        storyLines = res['lines']
        storyLines.append(line)
        col.update({'title': title}, {'title': title, 'lines': storyLines})

def getStory(title):
    res = col.find_one({'title': title})
    return res

def getAllStories():
    res = col.find()
    result = []
    for story in res:
        result.append(story)
    return result

def getAllStoryTitles():
    titles = []
    for story in getAllStories():
        titles.append(story['title'])
    return titles
    
def getStoryLines(title):
    return getStory(title)['lines']

def getAllStoryLines():
    allLines = []
    for story in getAllStoryTitles():
        for line in getStoryLines(story):
            allLines.append(line)
    return allLines

#def test():
#    auth()
#    addStory('hi')
#    print col.find_one()
#    addLine('hi', 'I like thluffy')
#    res=col.find_one({'title': 'hi'})
 #   print res['lines']
  #  addStory('bye')
#    addLine('bye', 'I like thluffy more')
 #   print getStoryLines('bye')
  #  print getAllStoryTitles()
  #  print getAllStoryLines()
  #  col.drop()
    
#test()
