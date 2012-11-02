from flask import Flask
from flask import url_for,redirect,flash
from flask import session, escape
from flask import request
from flask import render_template
from pymongo import connection
import util
from random import randrange

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    util.auth()
    global story
    global numberStories
    numberStories = 0
    for title in util.getAllStoryTitles():
        numberStories = numberStories + 1
    story = ""
    if request.method=="GET":
        return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)
    if request.method=="POST":
         button = request.form["button"]
         if button == "AddScramble":
             util.addStory(storyTitle)
             for line in storyScramble:
                 util.addLine(storyTitle, line)
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
         if button == "scramble":
            storyTitle = ""
            storyScramble = []

            for thing in util.getAllStoryTitles():
                storyTitle = storyTitle + " " + thing
            for thing in util.getAllStoryTitles():
                 storyScramble.append(util.getLine(thing, randrange(0,util.getNumberLines(thing))))
            return render_template("home.html", scrambledStory = storyScramble, scrambledStoryTitle = storyTitle)
                 
         if button:
             util.addLine(button,request.form["NextLine"])
             return render_template("home.html", giveTitles = util.getAllStoryTitles(), giveNumber = numberStories)

             

if __name__ == "__main__":
    app.run(debug = True)
        
