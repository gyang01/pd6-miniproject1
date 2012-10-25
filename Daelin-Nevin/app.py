#!usr/bin/python
from pymongo import Connection
from flask import Flask, render_template, url_for, redirect, request
import mongo

app = Flask(__name__)

mongo.startup()
global storyname	

@app.route("/", methods = ["GET", "POST"])
def home():
	global storyname
	storyname = ""
	if request.method == "GET":
		return render_template("home.html", stories = mongo.get_stories())
	else:
		button = request.form["button"]
		if button == "Go":
			storyname = str(request.form["storyselection"])
			return redirect(url_for("story"))
		if button == "Add":
			mongo.addstory(str(request.form["storyname"]))
			return render_template("home.html", stories = mongo.get_stories())

@app.route("/story", methods = ["GET", "POST"])
def story():
	if request.method == "GET":
		return render_template("story.html", story = storyname, lines = (mongo.get_story(storyname))[1:])
	else:
		button = request.form["button"]
		if button == "Submit":
			mongo.addline(storyname, str(request.form["line"]))
			return render_template("story.html", story = storyname, lines = (mongo.get_story(storyname))[1:])
		if button == "Cancel":
			global storyname
			storyname = ""
			return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug = True)
