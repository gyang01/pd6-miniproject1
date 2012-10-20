from pymongo import Connection

conn = Connection('mongo.stuycs.org')
#db = ''

def auth():
    db = conn.admin
    res = db.authenticate('ml7','ml7')

def start(): #or init
    auth()
    db = conn['Li-Robinson-mp1'] #name of database for this project
    
def add_story(storystart):
    db[storystart][storystart] = storystart #first line of story is story name
