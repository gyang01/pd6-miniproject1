from pymongo import Connection
Connection=Connection('mongo.stuycs.org')

# to auth
db = Connection.admin
res=db.authenticate('ml7','ml7')

# connect to database
db = Connection['Georgiana-Victoria']

stories=db.story_collection

def add_story(title="Example", line="a"):
    if not title in getTitles():
        lines=[a]
        story={'title':title,'lines'=lines}
        stories.insert(story)
    else:
        stories.update({'title':title}, {$push: {'lines':a} } )

def getTitles():
    res=[]
    #TBC
