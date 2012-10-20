from pymongo import Connection

conn = Connection('mongo.stuycs.org')

def auth():
    db = conn.admin
    res = db.authenticate('ml7','ml7')

def start(): #or init
    auth()
    #db = conn['Li-Robinson-mp1'] #name of database for this project
        
def add_story(storystart):
    db = conn['Li-Robinson-mp1']
    collection = db['stories']
    #if collection.find({'name':storystart}) == None: #try to check if the story exists
    collection.insert({'name':storystart, 'lines':[storystart]}) #first line of story is story title, and its key is its title; its lines are a list

def get_story(story):
    db = conn['Li-Robinson-mp1']
    collection = db['stories']
    res = collection.find_one({'name':story})
    if res:
        return res['lines']

def add_line(story,line):
    db = conn['Li-Robinson-mp1']
    collection = db['stories']
    res = collection.find_one({'name':story})
    if res:
        lines = res['lines']
        lines.append(line)
        collection.update({'name':story},{ '$set': {'lines':lines} })

#test
if __name__ == "__main__":
    story = 'Once upon a time'
    auth()
    db = conn['Li-Robinson-mp1']
    collection = db['stories']
    #add_story(story)
    #add_line(story,'In a land far far away')
    print db.collection_names()
    for line in collection.find(): print line
    print "done"
