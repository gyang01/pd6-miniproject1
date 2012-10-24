from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
from flask import session, escape

import unicodedata
import databasing

app = Flask(__name__)

allTitles = []
currTitle = ''
currLines = []

@app.route("/", methods=['GET', 'POST'])
def homepage():
    databasing.auth()
    global allTitles, currTitle, currLines
    if request.method=="GET":
        allTitles = databasing.get_titles()
        return render_template("homepage.html", allTitles=allTitles)
    else:
        story = str(request.form['story'])
        newStory = str(request.form['newStory'])

        button=request.form['button']
        if button=='go':
            if not story:
                flash('Please select a story!')
                return redirect(url_for('homepage'))
            else:
                currTitle = story
                currLines = databasing.get_lines(story)
                return redirect(url_for('story'))
        elif button=='create':
            if not newStory:
                flash('Please enter a new story title!')
                return redirect(url_for('homepage'))
            else:
                #check if title already exists (add method to databasing)
                databasing.add_title(story)
                currTitle = story
                currLines = databasing.get_lines(story)
                return redirect(url_for('addPage'))

@app.route("/story", methods=['GET', 'POST'])
def addPage():
    global allTitles, currTitle, currLines
    if request.method=="GET":
        return render_template("addPage.html", currTitle=currTitle, currLines=currLines)
    else:
        newLine = request.form['newLine']
        button = request.form['button']
        if button=='new':
            if not newLine:
                flash('Please enter a new line!')
                return redirect(url_for('addPage'))
            else:               
                databasing.add_line(currStory, newLine)
                return redirect(url_for('addPage'))
        elif button=='back':
            return redirect(url_for('homepage'))

if __name__=="__main__":
    app.debug=True 
    app.run(port=7000)
            

