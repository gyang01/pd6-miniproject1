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
<<<<<<< HEAD

def getTitles():
    res = stories.find()
    titles = []
    for line in res:
        titles.append(line['title'])
    return titles


def remove_story(title):
    res = stories.find()
    todelete = []
    for line in res:
        print 'In remove'
        print line
        if line['title'] == title:
            stories.remove(line)

def getAll():
    res = stories.find()
    for line in res:
        print line


=======
>>>>>>> cce95e694faf29ea6da47197eed254d1787c9069

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
<<<<<<< HEAD
    add_story('Example', 'a')


=======
    add_story('Example')
    #add_line('Example','a')
>>>>>>> cce95e694faf29ea6da47197eed254d1787c9069
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
<<<<<<< HEAD
getAll()
print 'After test'
remove_story('Example')
print 'After remove'
getAll()
print getTitles()
getAll()
#print getLines()
=======


>>>>>>> cce95e694faf29ea6da47197eed254d1787c9069
