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
    print collection.find_one({'title': title})['lines'][0].encode('utf8')

# get a list of all the story titles
def get_titles():
    global collection
    title_lines = collection.find()
    titles = []
    for line in title_lines:
        title = line['title'].encode('utf8')
        titles.append(title)
    print titles
    return titles

# get all lines of a story
def get_lines(title):
    global collection
    lines = collection.find_one({'title': title})['lines']
    for line in lines:
        print line
    return lines

# insert a new line into a story
def add_line(title, line):
  lines1 = get_lines(title)
  lines1.append(line)
  print lines1

#  collection.update({'title': title}, {'lines': lines1})
  

# collection.find_one({'title': title})['lines'].append(line)

# testing
auth()

add_title('story1', 'line1') 
add_title('story2', 'line2')

get_titles()

get_lines('story1')
get_lines('story2')

add_line('story2', 'line3')
get_lines('story2')
   #add more tests here


collection.drop()

