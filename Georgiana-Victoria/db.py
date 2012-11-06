from pymongo import Connection
Connection=Connection('mongo.stuycs.org')

# to auth
def auth():
	db = Connection.admin
	res=db.authenticate('ml7','ml7')
	# connect to database
	

def add_line(title="Example", line="a"):
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	if isTitle(title)<1:
		add_story(title)
	else:
		stories.update({'title':str(title)}, {"$push": {'lines':str(line)} } )

def add_story(title="Example"):
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	if not title in getTitles():
		story={"title":str(title),'lines':[]}
		stories.insert(story)

def isTitle(title="Example"):
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	return stories.find({'title':str(title)}).count()

def getTitles():
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	res = stories.find()
	titles = []
	for line in res:
		titles.append(line['title'])
	return titles


def remove_story(title):
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	res = stories.find()
	todelete = []
	for line in res:
		print 'In remove'
		print line
		if line['title'] == title:
			stories.remove(line)

def getLines(title):
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	res = stories.find()
	lines = []
	for line in res:
		if line['title'] == title:
			lines=line['lines']
	return lines

def getAll():
	db = Connection['Georgiana-Victoria']
	stories=db.story_collection
	res = stories.find()
	for line in res:
		print line

#TESTS

#stories.drop()
#def test():
#    add_story('Example')
#    add_line('Example','a')
#    add_line('Example','b')
#    add_story('Example')
#    add_story('Second Example')
#test()
#getAll()
#print 'After test'
#print getLines('Example')
#print 'After get lines'
#remove_story('Example')
#print 'After remove'
#getAll()
#print getTitles()
#getAll()
#print getLines()

