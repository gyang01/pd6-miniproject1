from pymongo import Connection

conn = Connection("mongo.stuycs.org")
def connect():
    db = conn.admin
    res = db.authenticate("ml7","ml7")
    
def add_new_story(title):
    db = conn["eric-claire"]
    stories = db.first_collection
    entry = {"title": title, "sentences": []}
    stories.insert(entry)
        
def add_sentence(title, sentence):
    db = conn["eric-claire"]
    stories = db.first_collection
    for line in stories.find():
        if line["title"]==title:
            tmp = line["sentences"]
            tmp.append(sentence)
            stories.update({"title":title}, {"title":title, "sentences":tmp})
            return
    print "Story not found: "+title
        
def list_stories():
    db = conn["eric-claire"]
    stories = db.first_collection
    result = []
    for story in stories.find():
        result.append(story["title"])
#        for sentence in story["sentences"]:
#            result += sentence + "\n"
#        result += "-----\n"
    return result

#connect()
