from pymongo import Connection 
Conn = Connection('mongo.stuycs.org')

def conn():	
	db = Conn.admin
	res = db.authenticate('ml7','ml7')
	db = Conn['z-pd6']
	stories = db.stories
	return stories

#this adds a new story called "title"
def addStory(title):
	stories = conn()
	stories.insert({'title': title, 'lines': []})

#this essentially deletes stories
def dropStory(title):
	stories = conn()
	stories.remove(stories.find_one({'title': title}))

#this gets all the stories in stories
def getStories():
	stories = conn()
	return [x['title'] for x in stories.find()]

#this adds line to the story
def addLine(title, line):
	stories = conn()
	stories.update({'title': title}, {'$push': {'lines': line}})

#this gets all lines added to the story
def getLines(title):
	stories = conn()
	return stories.find_one({'title': title})['lines']

if __name__=="__main__":
	#addStory('The best story ever')
	#addLine('The best story ever','It goes like this')
	dropStory('The best story ever')
	print getStories()
	#print getLines('The best story ever')
