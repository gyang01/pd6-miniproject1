from flask import Flask
from flask import render_template
from flask import request
from flask import url_for,redirect,flash
import mongo

app = Flask(__name__)
app.secret_key = 'super_secret'

m = mongo.mongo()


@app.route("/", methods=['GET','POST'])
def default():
    stories = mongo.mongo.getStories(m)
    if request.method=='GET':
        return render_template("default.html", stories=stories)
    if request.method=='POST':
        ns = str(request.form["newStory"])    
        b = request.form['button']
        if b=='Choose Story':
            storytitle = str(request.form["menu"])
            #lines = mongo.mongo.getLines(storytitle)
            return render_template("story.html", storytitle=storytitle)
        elif b == "Create Story":
            if not ns:
                stories = mongo.mongo.getStories(m)
                return render_template("default.html", stories=stories)
            else:
                mongo.mongo.newStory(m,ns)
                stories = mongo.mongo.getStories(m)
                return render_template("default.html", stories=stories)
        elif b == "Back":#not sure why this doesn't want to work
            stories = mongo.mongo.getStories(m)
            return render_template("default.html", stories=stories)
        elif b == "Save":#same here
            if not nl:
                return render_template("story.html", storytitle=storytitle)
            else:
                nl = str(request.form["newStory"])
                storytitle = str(request.form["menu"])
                mongo.mongo.newLine(storytitle,nl)
                return render_template("default.html", storytitle=storytitle)

        

if __name__ == "__main__":
    app.debug = True
    app.run()


