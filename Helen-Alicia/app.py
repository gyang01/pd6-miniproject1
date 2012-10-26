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
currLines = []

@app.route("/", methods=['GET', 'POST'])
def homepage():
    databasing.auth()
    global allTitles, currTitle, currLines
    if request.method=="GET":
        allTitles = databasing.get_titles()
        print(allTitles)
        allTitles.append('')
        return render_template("homepage.html", allTitles=allTitles)
    else:
        story=request.form['stories']
        print("got story!" + story)
        newStory=request.form['newStory']
        print("got new story!" + newStory)

        button=request.form['button']
        if button=='go':
            if story == '':
                print("pressed go but no story")
                flash('Please select a story!')
                return redirect(url_for('homepage'))
            else:
                print("pressed go and has story")
                currTitle = story
                currLines = databasing.get_lines(story)
                return redirect(url_for('addPage'))
        elif button=='create':
            if newStory == "new story":
                print("clicked create!")
                flash('Please enter a new story title!')
                return redirect(url_for('homepage'))
            else:
                #check if title already exists (add method to databasing)
                print("else!")
                databasing.add_title(story)
                currTitle = story
                print(currTitle)
                currLines = databasing.get_lines(story)
                return redirect(url_for('addPage'))

@app.route("/addPage", methods=['GET', 'POST'])
def addPage():
    databasing.auth()
    global allTitles, currTitle, currLines
    if request.method=="GET":
        return render_template("addPage.html", currTitle=currTitle, currLines=currLines)
    else:
        newLine=request.form['newLine']
        button=request.form['button']
        if button=='new':
            if newLine == "new line":
                flash('Please enter a new line!')
                return redirect(url_for('addPage'))
            else:               
                databasing.add_line(currStory, newLine)
                return redirect(url_for('addPage'))
        elif button=='back':
            return redirect(url_for('homepage'))

if __name__=="__main__":
    app.debug=True 
    app.run(port=5000)
            

