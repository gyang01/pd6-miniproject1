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
            


if __name__ == "__main__":
    app.debug=True
    app.run()
