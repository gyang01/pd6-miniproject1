from pymongo import Connection

conn = Connection("mongo.stuycs.org")
db = conn.admin
res = db.authenticate("ml7","ml7")

db = conn["eric-claire"]
stories = db.first_collection
db.drop_collection(stories)

def add_new_story(title):
    entry = {"title": title, "sentences": []}
    stories.insert(entry)

#def add_sentence(story, sentence):
    

def list_stories():
    result = ""
    for story in stories.find({}, {"title":"a"}):
        result += story["title"]+"\n"
    return result

add_new_story("one")
add_new_story("two")
add_new_story("three")
print list_stories()
