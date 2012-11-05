from pymongo import Connection

class db:
	def __init__(self):
		self.connection = Connection('mongo.stuycs.org')
		self.db = self.connection.admin
		self.db.authenticate('ml7','ml7')
		self.db = self.connection['z-demo-mini-pd6']

#this adds a new story called "title"
def addStory(self, title):
	self.db.stories.insert({'title': title, 'lines': []})

#this essentially deletes stories
def dropStoreis(self):
	self.db.stories.drop()

#this gets all the stories in stories
def getStories():
	return [x['title'] for x in self.db.stories.find()]

#this adds line to the story
def addLine(self, story, line):
	clct = self.db.stories
	s = [x for x in clct.find({'title': story})]
	if len(s) != 1:
		return
	d = s[0]
	print d[]
	d['lines'].append(line)
	clct.update({'title': story}, d)

#this gets all lines added to the story
def getLines(self, story):
	clct = self.db.stories
	return clct.find({'title': story})[0]['lines']

if __name__=="__main__":
	addStories('The best story ever')
	addLine('It goes like this')
