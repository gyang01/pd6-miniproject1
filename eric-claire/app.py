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
        elif button == "View Story":
            title = str(request.form["view_one"])
            print title
            lines = database.get_lines(title)
            return render_template("home.html",title=title,lines=lines)
        elif button == "Drop story":
            database.remove_one() ###come back to this later
            titles=database.list_stories()
            return render_template("home.html",titles=titles)


if __name__ == "__main__":
    app.debug=True
    app.run()
