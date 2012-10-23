from pymongo import Connection

def connect():
	conn = Connection('mongo.stuycs.org')
	db = conn.admin
	res = db.authenticate("ml7", "ml7")
	db = conn["z-pd6-Adam-Izzi"]
	return db

#this adds a new story called "title"
def addStory(title):
	db = connect()
	db.stories.save({"title": title, "lines": []})

#this adds line to the story
def addLine(title, line):
	db = connect()
	story = db.find({"title": title})
	story[lines].append(line)
	stories.remove({"title": title})
	stories.insert(story)

#this gets all the stories in stories
def getStories():
	db = connect()
	storylist = []
	for story in stories.find():
		if "title" in story.keys():
			storylist.append(story["title"])
	return storylist

#this gets all lines added to the story
def getLines(title):
	db = connect()
	for story in stories.find({"title": title}):
		return story["lines"]
