from pymongo import Connection

def connect():
	Connection = Connection('mongo.stuycs.org')
	db = Connection.admin
	db.authenticate("ml7", "ml7")
	db = Connection["Izzam"]
	return db


#this adds a new story called "title"
def addStory(title):
	db.stories.save({title: title, lines: []})





