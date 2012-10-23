from flask import Flask,render_template,request,redirect,url_for
import util

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    util.auth()
    if request.method == 'GET':
        titles = util.get_story_titles()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Go":
            pass
        elif button == "Create":
            storyname = request.form["new_story"]
            util.add_story(storyname)
            titles = util.get_story_titles()
            return render_template("home.html",titles=titles)
