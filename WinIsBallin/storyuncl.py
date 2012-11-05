from pymongo import Connection

#Comm-link established
conn = Connection('mongo.stuycs.org')

#I am ADMIN
db = conn.admin
AUTHENTICATION = db.authenticate('ml7','ml7')
#Lets go period 6
db = conn['z-pd6']
#Our storybook <3
col = db["WinBall's StoryBook"]

def newStory(name):
	col.save({'name': name, 'text': ["Not Started Yet"]})

def getStories():
	stories = []
	for line in col.find():
 		stories.append(str(line['name']))
	return stories

def getStory(name):
        return col.find({'name':name})[0]

def getText(story):
	return getStory(story)['text']

def addLine(story, newline):
	#if(getText(story)[0] == "Not Started Yet"):
		#col.update({'name': story}, {'text': newline})
	col.update({'name': story}, {'$push': {'text': newline}})
	return getStory(story)

def dropone(story):
	col.remove({'name': story})

def dropall():
	col.remove()




col.remove({'text': "hello"})
#col.save({'name': "asdf", 'lines': 0, 'text': ["Not Yet Started"]})


