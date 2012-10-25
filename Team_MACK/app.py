from util import *
from flask import Flask, render_template, session, url_for, request, escape, redirect, g

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
db = DatabaseConnection()

@app.route("/", methods=["GET", "POST"])
def ind():
    if request.method == "POST":
        if "story_menu" in request.form:
            return redirect(url_for("story_page", story=request.form["story_menu"]))
        else:
            story_name = request.form["add_story_field"]
            if story_name:
                db.addStory(story_name)
    return render_template("index.html", stories=db.getStories())

@app.route("/<story>", methods=["GET", "POST"])
def storyPage(story):
    if request.method == "POST":
        db.addLine(story, request.form["add_line_field"])
    return render_template("story.html", lines=db.getStory(story))

@app.route("/drop/stories")
def dropPage():
    db.removeStories()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
