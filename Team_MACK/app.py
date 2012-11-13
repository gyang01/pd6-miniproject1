from flask import Flask
from flask import render_template, url_for, request, escape, redirect
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
    if request.method == "GET":
        return render_template("select.html", stories=getStories(db))   

@app.route("/<story>", methods=["GET", "POST"])
def story_page(story):
    if request.method == "POST":
        button=request.form.get('button', None)
        if (button=="Add Line"):
            addLine(db, story, request.form.get('newLine',""))
            return render_template("story.html", lines=getStory(db, story))
        elif (button=="back"):
            return redirect(url_for('/'))
    if request.method == "GET":
        return render_template("story.html", lines=getStory(db, story))


@app.route("/drop/stories")
def dropcurr():
    removeStories(db)
    return redirect(url_for("selection"))

@app.route("/drop/story")
def dropthis(story):
    removeStory(db, story)
    return redirect(url_for("selection"))

@app.route("/drop/story/line")
def dropline(story, index):
    removeLine(db, story, index)
    return redirect(url_for("story_page", story = story))

if __name__ == "__main__":
<<<<<<< HEAD
    app.run()   
=======
    app.debug=True
    app.run()
>>>>>>> back button still doesn't work
