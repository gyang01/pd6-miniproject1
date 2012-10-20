from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

# to auth
db = Connection.admin
res = db.authenticate('ml7', 'ml7')

# connect to your own database
db = Connection['z-pd6']
collection = db['HA']

# get a list of all the story titles
def get_titles():
    title_lines = collection.find()
    titles = []
    for line in title_lines:
        title = line['title'].encode('utf8')
        titles.append(title)
    print titles
    return titles

# get all lines of a story
def get_lines(title):
    lines = collection.find_one({'title': title})['lines']
    for line in lines:
        print line
    return lines

# insert a new line into a story


# testing
collection.insert({'title': 'story1', 'lines': ['S1L1', 'S1L2']}) 
collection.insert({'title': 'story2', 'lines': ['S2L2', 'S2L2']})

get_titles()
get_lines("story1")

   #add more tests here

collection.drop()

