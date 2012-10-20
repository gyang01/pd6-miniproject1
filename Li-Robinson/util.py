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
    collection = db['stories'] #name of collection of stories
    
def add_story(storystart):
    collection.insert({'name':storystart, 'lines':[storystart]}) #first line of story is story title, and its key is its title; its lines are a list

def get_story(story):
    res = collection.find_one({'name':story})
    if res:
        return res['lines']

def add_line(story,line):
    res = collection.find_one({'name':story})
    #lines = res['lines']
    print res#['lines']
    #lines.append(line)
    #collection.update({'name':story},{ '$set': {'lines':lines} })

#test
if __name__ == "__main__":
    story = 'There once was a'
    start()
    for line in db.collection.find(): print line
    #print db.collection_names()
    #add_story('There once was a')
    #add_line(story,'Man named Fred')
    #print get_story(story)
