from flask import Flask, render_template
from flask import request, redirect, url_for
import database

app = Flask(__name__)
global current_story

@app.route("/",methods=["GET", "POST"])
def home():
    global current_story
    database.connect()
    if request.method == "GET":
        titles = database.list_stories()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Create":
            newtitle = request.form.get("newStory", "Untitled")
            database.add_new_story(newtitle)
            lines = database.get_lines(newtitle)
            current_story = newtitle
            return render_template("home.html",title=newtitle,lines=lines)
        elif button == "View story":
            title = str(request.form["view_one"])
            current_story = title
            lines = database.get_lines(title)
            return render_template("home.html",title=title,lines=lines)
        elif button == "Drop story":
            title = request.form["view_one"]
            database.remove_one(title)
            titles=database.list_stories()
            return render_template("home.html",titles=titles)
        elif button == "Add line":
            newLine = request.form.get("newLine", "")
            title = current_story
            database.add_sentence(title,newLine)
            lines = database.get_lines(title)
            return render_template("home.html",title=title,lines=lines)
        elif button == "Back":
            titles = database.list_stories()
            return render_template("home.html",titles=titles)

if __name__ == "__main__":
    app.debug=True
    app.run()
