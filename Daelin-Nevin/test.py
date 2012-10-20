#!usr/bin/python
import mongo

if __name__ == "__main__":
	mongo.startup()
	mongo.addstory("tale of something")
	mongo.addline("tale of something", "some stuff happened somewhere")
	mongo.addline("tale of something", "at sometime")
	for story in mongo.get_stories():
		print story
	print
	for line in  mongo.get_story("tale of something"):
		print line
	

