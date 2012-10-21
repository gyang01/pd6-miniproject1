from pymongo import Connection
Connection=Connection('mongo.stuycs.org')

# to auth
db = Connection.admin
res=db.authenticate('ml7','ml7')

# connect to database
db = Connection['Georgiana-Victoria']

stories=db.story_collection
titles=[]

def add_line(title="Example", line="a"):
    if not title in getTitles():
        add_story(title)
    else:
        stories.update({'title':str(title)}, {"$push": {'lines':str(line)} } )

def add_story(title="Example"):
    if not title in getTitles():
        titles.append(str(title))
        lines=[str(line)]
        story={'title':str(title),'lines':str(lines)}
        stories.insert(story)

def getTitles():
    return titles

#res = stories.find()
#for line in res:
#    print line
#print getTitles()
