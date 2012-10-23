from pymongo import Connection

conn = Connection("mongo.stuycs.org")
db = conn.admin
res = db.authenticate("ml7","ml7")

db = conn["eric-claire"]
stories = db.first_collection
db.drop_collection(stories)

def add_new_story(title):
    if stories.find({"title":title}).count() == 0:
        entry = {"title": title, "sentences": []}
        stories.save(entry)

def add_sentence(title, sentence):
    for line in stories.find():
        if line["title"]==title:
            tmp = line["sentences"]
            tmp.append(sentence)
            stories.update({"title":title}, {"title":title, "sentences":tmp})
            return
    print "Story not found: "+title

def list_stories():
    result = ""
    for story in stories.find():
        result += "*"+story["title"] + "*\n"
        for sentence in story["sentences"]:
            result += sentence + "\n"
        result += "-----\n"
    return result

add_new_story("eric")
add_new_story("eric") #I don't allow dupes
add_new_story("claire")
add_new_story("fred")
add_sentence("thluffy", "hey!")
add_sentence("fred", "once upon a time")
add_sentence("fred", "I enrolled in ml7")
print list_stories()
#for line in stories.find():
#    print line
