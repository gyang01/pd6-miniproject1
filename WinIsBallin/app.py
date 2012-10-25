from flask import Flask
from flask import render_template
from flask import request
from flask import url_for,redirect

import story

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html', stuff="stuff")
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
    else:
        db = story.db()
        button = request.form['button']
        if button == "Create!":
            db.newStory(request.form['title'])
            return redirect(url_for('home'))
	

@app.route("/cont", methods = ['GET', 'POST'])
def cont():
    db = story.db()
    stories = db.getStoryNames()
    if request.method=="GET": 
	selectedstory=[]
	return render_template("continue.html", stories=stories,selectedstory=selectedstory)
    else:
        button = request.form['button']
        if button == "Add to Story":
            name = request.form['story'] 
            selectedstory = db.getText(name)
            return render_template("continue.html", stories=stories,selectedstory=selectedstory)
     
    
@app.route("/drop", methods = ['GET', 'POST'])
def drop():
    if request.method=="GET":
	return render_template("drop.html")
    else:
        db = story.db()
        button = request.form['button']
        if button == "Drop this Story":
            name = request.form['story']
            db.remove(name)
            return render_template("home.html")



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
    
