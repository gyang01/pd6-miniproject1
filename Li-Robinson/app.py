from flask import Flask,render_template
import util

app = Flask(__name__)

@app.route("/")
def home():
    util.auth()
    titles = util.get_story_titles()
    return render_template("home.html",titles=titles)
