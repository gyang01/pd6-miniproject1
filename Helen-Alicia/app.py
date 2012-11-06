from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
from flask import session, escape

import unicodedata
import databasing

app = Flask(__name__)
app.secret_key = 'some_secret'

allTitles = []
currTitle = ''

databasing.auth()

@app.route("/", methods=['GET', 'POST'])
def homepage():
    global allTitles, currTitle
    if request.method=="GET":
        allTitles = databasing.get_titles()
        return render_template("homepage.html", allTitles=allTitles)
    else:
        story=request.form.get('stories', "")
        newStory=request.form.get('newStory', "")
   
        button=request.form.get('button', None)
        if button=='go':
            currTitle = story
            return redirect(url_for('addPage'))
        elif button=='create':
            if databasing.exists(newStory):
                flash("story already exists!")
                return redirect(url_for('homepage'))
            else:
                databasing.add_title(newStory)
                currTitle = newStory
                return redirect(url_for('addPage'))

@app.route("/addPage", methods=['GET', 'POST'])
def addPage():
    global allTitles, currTitle
    if request.method=="GET":
        currLines = databasing.get_lines(currTitle)
        return render_template("addPage.html", currTitle=currTitle, currLines=currLines)
    else:
        newLine=request.form.get('newLine', "")
        button=request.form.get('button', None)

        if button=='new':
            databasing.add_line(currTitle, newLine)
            return redirect(url_for('addPage'))
        elif button=='back':
            return redirect(url_for('homepage'))

if __name__=="__main__":
    app.debug=True 
    app.run(port=5000)
            

