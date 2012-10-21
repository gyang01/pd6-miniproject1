from pymongo import Connection
Connection=Connection('mongo.stuycs.org')

# to auth
db = Connection.admin
res=db.authenticate('ml7','ml7')

# connect to database
db = Connection['Georgiana-Victoria']

stories=db.story_collection

def add_line(title="Example", line="a"):
    if isTitle(title)<1:
        add_story(title)
    else:
        stories.update({'title':str(title)}, {"$push": {'lines':str(line)} } )

def add_story(title="Example"):
    if isTitle(title)<1:
        story={"title":str(title),'lines':[]}
        stories.insert(story)
    else:
        pass

def isTitle(title="Example"):
    return stories.find({'title':str(title)}).count()

#stories.drop()
def test():
    add_story('Example')
    #add_line('Example','a')
test()
res = stories.find()
for line in res:
    print line
def getTitles():
    l=[]
    res = stories.find()
    for r in res:
        l.append(r['title'])
    return l
print getTitles()


