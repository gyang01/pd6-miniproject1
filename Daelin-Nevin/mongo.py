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
	db = con["z-pd6"]
	global col
	col = db["DaNe"]
	res = col.find()

def addstory(name):
	global col
	res = col.find()
	for entry in res:
		if entry["name"] == name:
			return
	story = {"name": name, "line":"0", "text":name}
	col.insert(story)

def addline(story, line):
	global col
	res = col.find()
	ln = 0
	for entry in res:
		if entry["name"] == story:
			ln+= 1
	newline = {"name":story, "line":str(ln), "text":line}
	col.insert(newline)

def get_story(story):
	res = col.find()
	ret = []
	for entry in res:
		if entry["name"] == story:
			ret.append(entry)
	return ret

def get_stories():
	res = col.find()
	ret = [];
	for entry in ret:
		if entry["line"] == "0":
			ret.append(entry)
	return ret
