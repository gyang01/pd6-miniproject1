from pymongo import Connection

conn = Connection('mongo.stuycs.org')
global db
global collection

def auth():
    global db
    db = conn.admin
    res = db.authenticate('ml7','ml7')

def start(): #or init
    auth()
    db = conn['Li-Robinson-mp1'] #name of database for this project
    global collection
    collection = db['stories']
    
def add_story(storystart):
   # global collection
    #collection = db['stories']
    collection.insert({'lines':[storystart]}) #first line of story is story name

def get_story(storyname):
    #global collection
    #collection = db['stories']
    for thing in collection.find():
        print thing['lines']

#test
if __name__ == "__main__":
    start()
    global collection
    collectino = db['There once was a']
    collection.drop()
    #add_story('There once was a')
    #print get_story('There once was a')
