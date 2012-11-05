from flask import Flask
from flask import render_template
from flask import request
from flask import url_for,redirect
from pymongo import Connection

import story
import storyuncl

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home(msg = ""):

    if request.method == "GET":
        return render_template('home.html', stuff = msg)
    else:
        button = request.form['button']
        if button == "Create a New Story":
            return redirect(url_for('create'))
        elif button == "Continue a Story":
            return redirect(url_for('cont'))
	elif button == "Drop a Story":
            return redirect(url_for('drop'))


@app.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html')

    button = request.form['button']
    if button == "Create!":
        storyuncl.newStory(request.form['title'])
        return redirect(url_for('home'))
	

@app.route("/cont", methods = ['GET', 'POST'])
def cont():
    stories = storyuncl.getStories()
    if request.method=="GET": 
	return render_template("continue.html", stories=stories)
    else:
	button = request.form['button']
	if button == "Show text":
            name = request.form['story']
	    print name
            storytext = storyuncl.getText(name)
            return render_template("continue.html", stories=stories,storytext=storytext)
	if button == "Add to Story":
		name = request.form['story']
		if (request.form['newline'] != ""):
			storyuncl.addLine(request.form['story'], request.form['newline'])
			storytext = storyuncl.getText(name)
			return render_template("continue.html", stories=stories,storytext=storytext)
	if button == "Cancel":
		return redirect(url_for('home'))
    
    
@app.route("/drop", methods = ['GET', 'POST'])
def drop():
    stories = storyuncl.getStories()
    if request.method=="GET":
	return render_template("drop.html", stories=stories)
    else:
        button = request.form['button']
        if button == "Drop this Story":
            name = request.form['story']
	    print name
            storyuncl.dropone(name)
            return redirect(url_for('drop'))
	if button == "Drop All Stories":
            storyuncl.dropall()
            return redirect(url_for('home'))
	if button == "Cancel":
		return redirect(url_for('home'))



#@app.route("/stories", methods = ['GET', 'POST'])
#def stories():
 #   if request.method == 'GET':
  #      db = story.db()
  #      titles = db.getStoryNames()
  #      return render_template('continue.html', titles=titles) 
  #  elif request.method == 'POST':
  #      title = request.form['titles']
  #      return redirect(url_for('continue.html'))
            
        
if __name__ == '__main__':
    app.debug = True
    app.run()
    
