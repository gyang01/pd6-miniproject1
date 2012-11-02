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
    global numberStories
    numberStories = 0
    for title in util.getAllStoryTitles():
        numberStories++
    story = ""
    if request.method=="GET":
        return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)
    if request.method=="POST":
         button = request.form["button"]
         if button == "Ok":
             story = str(request.form["storySelection"])
             return render_template("home.html", titleStory = story, giveLines = util.getStoryLines(story), giveNumber = numberStories)
         if button == "Add":
             story = request.form["NewStory"]
             util.addStory(story)
             return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)
         if button == "DropStories":
             util.dropStories()
             return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)
         if button:
             util.addLine(button,request.form["NextLine"])
             return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)

             

if __name__ == "__main__":
    app.run(debug = True)
        
