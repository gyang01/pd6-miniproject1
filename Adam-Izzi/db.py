from flask import Flask,render_template, url_for,redirect,request

class db:
	def __init__(self):
		self.connection = Connection('mongo.stuycs.org')
		self.db = self.connection.admin
		self.db.authenticate('ml7','ml7')
		self.db = self.connection['z-pd6']

#this adds a new story called "title"
def addStory(self, title):
	self.db.stories.insert({'title': title, 'lines': []})

#this essentially deletes stories
def dropStories(self):
	self.db.stories.drop()

#this gets all the stories in stories
def getStories():
	return [x['title'] for x in self.db.stories.find()]

#this adds line to the story
def addLine(self, story, line):
	clct = self.db.stories
	s = [x for x in clct.find({'title': story})][0]
	clct.remove({'_id':story['_id']})
	clct.insert(s)

#this gets all lines added to the story
def getLines(self, story):
	clct = self.db.stories
	return clct.find({'title': story})[0]['lines']

if __name__=="__main__":
	addStories('The best story ever')
	addLine('It goes like this')
