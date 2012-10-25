from util import *
from flask import Flask, render_template, session, url_for, request, escape, redirect, g
from database import *

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
db = DatabaseConnection()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "story_menu" in request.form:
            return redirect(url_for("story_page", story=request.form["story_menu"]))
        else:
            story_name = request.form["add_story_field"]
            if story_name:
                addStory(db, story_name)
    return render_template("index.html", stories=getStories(db))

@app.route("/<story>", methods=["GET", "POST"])
def storyPage(story):
    if request.method == "POST":
        addLine(db, story, request.form["add_line_field"])
    return render_template("story.html", lines=getStory(db, story))

@app.route("/drop/stories")
def dropPage():
    removeStories(db)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
