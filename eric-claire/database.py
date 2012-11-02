from pymongo import Connection

conn = Connection("mongo.stuycs.org")
def connect():
    db = conn.admin
    res = db.authenticate("ml7","ml7")

def add_new_story(basetitle):
    db = conn["eric-claire"]
    stories = db.first_collection
    if basetitle == "": #Blank titles are ugly
        basetitle = "Untitled"
    title=basetitle #ready to be checked for duplicates
    info = [line for line in stories.find()]
    titles = [str(line["title"]) for line in info]
    a=0 #what number the story will be (original title = unnumbered)
    while title in titles:
        title = basetitle
        title = title + " "+ str(a)
        a=a+1
    entry = {"title": title, "sentences": [""]}
    stories.insert(entry)
    return title #important because title doesn't always match basetitle
        
def add_sentence(title, sentence):
    db = conn["eric-claire"]
    stories = db.first_collection
    for line in stories.find():
        if line["title"]==title:
            tmp = line["sentences"]
            tmp.append(sentence)
            stories.update({"title":title}, {"title":title, "sentences":tmp})
            return

def get_lines(title):
    db = conn["eric-claire"]
    stories = db.first_collection
    for line in stories.find():
        if line["title"]==title:
            return line["sentences"]

def list_stories():
    db = conn["eric-claire"]
    stories = db.first_collection
    result = [story["title"] for story in stories.find()]
    return result

def remove_one(title):
    db = conn["eric-claire"]
    stories = db.first_collection
    lines = stories.find()
    for line in lines:
        if line["title"] == title:
            stories.remove(line)

#connect()
