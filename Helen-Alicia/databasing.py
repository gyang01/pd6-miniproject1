from pymongo import Connection

global connection, db, res, collection 


def auth():
    global connection, db, res, collection    
    connection = Connection('mongo.stuycs.org')

    db = connection.admin
    res = db.authenticate('ml7', 'ml7')

    db = connection['z-pd6']
    collection = db['HA']

# adds a story title
def add_title(title, line):    
    global collection
    collection.insert({'title': title, 'lines': [line]})
    print collection.find_one({'title': title})['title'].encode('utf8') + ' - ' + collection.find_one({'title': title})['lines'][0].encode('utf8')

# get a list of all the story titles
def get_titles():
    global collection
    lines = collection.find()
    titles = []
    for line in lines:
        title = line['title'].encode('utf8')
        titles.append(title)
    print titles
    return titles

# get all lines of a story
def get_lines(title):
    global collection
    uLines = collection.find_one({'title': title})['lines']
    lines = []
    for uLine in uLines:
        line = uLine.encode('utf8')
        lines.append(line)
    print lines
    return lines

# insert a new line into a story
def add_line(title, line):
  lines1 = collection.find_one({'title': title})['lines']
  lines1.append(line)
  collection.update({'title': title}, {'title': title, 'lines': lines1})
  print 'added new line to ' + title

# testing
auth()

add_title('story1', 'S1L1') 
add_title('story2', 'S2L1')

get_titles()

get_lines('story1')
get_lines('story2')

add_line('story1', 'S1L2')
add_line('story2', 'S2L2')

get_lines('story1')
get_lines('story2')

collection.drop()

