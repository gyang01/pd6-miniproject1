from pymongo import Connection

global connection, db, res, collection 


def auth():
    global connection, db, res, collection    
    connection = Connection('mongo.stuycs.org')

    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    print res

    db = connection['z-pd6']
    collection = db['HA']

# adds a story title
def add_title(title):    
    global collection
    collection.insert({'title': title, 'lines': []})
    #print collection.find_one({'title': title})['title'].encode('utf8')

# get a list of all the story titles
def get_titles():
    global collection
    titles = [line['title'].encode('utf8') for line in collection.find()]
    return titles
    
# returns all lines of a story
def get_lines(title):
    global collection
    uLines = collection.find_one({'title': title})['lines']
    lines = []
    for uLine in uLines:
        line = uLine.encode('utf8')
        lines.append(line)
    print "got lines!" 
    print lines
    return lines

# insert a new line into a story
def add_line(title, line):
    global collection
    lines1 = collection.find_one({'title': title})['lines']
    lines1.append(line)
    collection.update({'title': title}, {'title': title, 'lines': lines1})

# return true if title already exists

def exists(title):
    global collection
    return not collection.find_one({'title': title}) == None
    
# drop all titles
def drop_all_titles():
    global collection
    collection.drop()


# testing

#print auth()

#print exists('OneWordTitle')

#add_title('story1') 
#add_title('story2')

#print get_titles()

#get_lines('story1')
#get_lines('story2')

#add_line('story1', 'S1L1')
#add_line('story2', 'S2L1')

#get_lines('story1')
#get_lines('story2')

#print drop_all_titles()

