from flask import Flask
from flask import url_for,redirect,flash
from flask import session, escape
from flask import request
from flask import render_template
from pymongo import connection
import util

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    util.auth()
    global story
    story = ""
    if request.method=="GET":
        return render_template("home.html", titles = util.getAllStoryTitles())
    if request.method=="POST":
         button = request.form["button"]
         if button == "Ok":
             story = str(request.form["story"])
             return redirect(url_for("story"))
         if button == "Add":
             util.addstory(str(request.form["NewStory"]))
             return render_template("home.html", titles = util.getAllStoryTitles())
             

@app.route("/story", methods = ["GET", "POST"])
def story():
    if NewStory == "":
        NewStory = "Wow you suck you didn't give a title"
    if request.method == "GET":
        return render_template("story.html", story = story, StoryLines = util.getStoryLines(story))
    if request.method == "POST":
        a = request.form["button"]
        if a == AddTheLine:
            util.addLine(story, AddLine)
            return render_template("home.html", titles = util.getAllStoryTitles())

if __name__ == "__main__":
	app.run(debug = True)
