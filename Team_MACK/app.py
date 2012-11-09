from flask import Flask
from flask import render_template, url_for, request, escape, redirect, g
from database import *

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
db = startConnection().mack

@app.route("/", methods=["GET", "POST"])
def selection():
    if request.method == "POST":
        if "story_menu" in request.form:
            return redirect(url_for("story_page"
                                    ,story = request.form["story_menu"]))
        else:
            story_name = request.form["add_story_field"]
            if story_name:
                addStory(db, story_name)
    return render_template("select.html", stories=getStories(db))

@app.route("/<story>", methods=["GET", "POST", "LINK"])
def story_page(story):
    a = 0
    if request.method == "POST":
        addLine(db, story, request.form["add_line_field"])
        a = 1
    if request.method == "LINK":
        a = 2
        print a
    if (a < 2):
        return render_template("story.html", lines=getStory(db, story))
    else:
        return render_template("select.html", stories=getStories(db))


@app.route("/drop/stories")
def dropcurr():
    removeStories(db)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
