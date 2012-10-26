from flask import Flask, render_template
from flask import request
import database

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def home():
    database.connect()
    if request.method == "GET":
        titles = database.list_stories()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Create":
            newtitle = request.form.get("newStory", "Untitled")
            database.add_new_story(newtitle)
            titles = database.list_stories()
            return render_template("home.html",titles=titles)
        elif button == "View story":
            title = str(request.form["view_one"])
            lines = database.get_lines(title)
            print lines
            return render_template("home.html",title=title,lines=lines)
        elif button == "Drop story":
            title = request.form["view_one"]
            database.remove_one(title) ###come back to this later
            titles=database.list_stories()
            return render_template("home.html",titles=titles)
        elif button == "Back":
            titles = database.list_stories()
            return render_template("home.html",titles=titles)

if __name__ == "__main__":
    app.debug=True
    app.run()
