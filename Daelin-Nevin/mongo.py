#!usr/bin/python
from pymongo import Connection

con = Connection("mongo.stuycs.org")

global db
global res
global col

def startup():
	db = con.admin
	res = db.authenticate("ml7","ml7")
	db = con["z-pd6"]
	col = db["DaNe"]

def addstory(name):
	story = {"name": name, "line":"0", "text":name}
	db.insert(story)

def addline(story, line):
	res = col.find()
	ln = 0
	for entry in res:
		if entry["name"] == story:
			ln+= 1
	newline = {"name":story, "line":str(ln), "text":line}
	db.insert(newline)

def get_stories():
	ret = [];
	res = col.find()
	for entry in ret:
		if entry["line"] == "0":
			ret.append(entry)
	return ret
