from pymongo import Connection
Connection=Connection('mongo.stuycs.org')

# to auth
db = Connection.admin
res=db.authenticate('ml7','ml7')

# connect to database
db = Connection['Georgiana-Victoria']

stories=db.story_collection
titles=[]
def add_story(title, line):
    if not title in titles:
        titles.append(str(title))
        lines=[str(line)]
        story={'title':str(title),'lines':str(lines)}
        stories.insert(story)
    else:
        stories.update({'title':str(title)}, {"$push": {'lines':str(line)} } )
def getTitles():
    return titles
#res = stories.find()
#for line in res:
#    print line

def test():
    add_story('Example', 'a')
test()
print getTitles()
