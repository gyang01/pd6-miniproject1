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
<<<<<<< HEAD
        if button == "Create a New Story":
            	return redirect(url_for('create'))
>>>>>>> 097b3e5d1869d4dbec12796d439990aaf807f13f
        elif button == "Continue a Story":
		return redirect(url_for('cont'))
	elif button == "Drop a Story":
		return redirect(url_for('drop'))


@app.route("/create", methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html')
    else:
        button = request.form['button']
        if button == "Create!":
            story.newStory(request.form['title'])
            return redirect(url_for('home'))
	

@app.route("/cont")
def cont():
    if request.method=="GET":
	stories=[["Goodbye"], ["Cruel World!"]]
	selectedstory=["Hello World!", "Goodbye!", 1,2,3,4,5,6]
	return render_template("continue.html", stories=stories,selectedstory=selectedstory)

@app.route("/drop")
def drop():
    if request.method=="GET":
	return render_template("drop.html")

@app.route("/stories", methods = ['GET', 'POST'])
def stories():
    if request.method == 'GET':
        db = story.db()
        titles = db.getStoryNames()
        return render_template('continue.html', titles=titles) 
    elif request.method == 'POST':
        title = request.form['titles']
        return redirect(url_for('continue.html'))
            
#@app.route("/storyadd", methods = ['GET', 'POST'])
#def storyadd():
#    if request.method == 'GET':

@app.route("/drop")
def drop():
    if request.method == 'GET':
        return render_template('drop.html')
        
        
if __name__ == '__main__':
    app.debug = True
    app.run()

