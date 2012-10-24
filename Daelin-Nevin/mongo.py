#!usr/bin/python
from pymongo import Connection

global con
con = Connection("mongo.stuycs.org")

global db
global res
global col

def startup():
	global db
	db = con.admin
	global res
	res = db.authenticate("ml7","ml7")
	db = con["DaNe"]
	global col
	col = db["DaNestories"]
	res = col.find()

def addstory(name):
	global col
	res = col.find({"name":name})
	for entry in res:
		return
	story = {"name": name, "line":"0", "text":name}
	col.insert(story)

def addline(story, line):
	global col
	res = col.find({"name":story})
	ln = 0
	for entry in res:
		ln+= 1
	newline = {"name":story, "line":str(ln), "text":line}
	col.insert(newline)

def get_story(story):
	res = col.find({"name":story})
	return [x["text"] for x in res]

def get_stories():
	res = col.find({"line":"0"})
	return [x["name"] for x in res]
