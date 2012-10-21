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
    

def test():
    auth()
    addStory('hi')
    print col.find_one()
    addLine('hi', 'I like cheese')
    res=col.find_one({'title': 'hi'})
    print res['lines']
    col.drop()

test()
