from flask import Flask
from flask import render_template
from flask import request

import story

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
<<<<<<< HEAD
        return render_template('home.html', stuff="stuff")
    button = request.form['button']
    if button == "Create New Story":
	return redirect(url_for('createStory'))
=======
        db = story.db()
        titles = []
        for title in db.getStoryNames():
            titles.append()
        return render_template('home.html', titles=titles)
        
    if request.form['button'] == "Create New Story":
	return redirect(url_for('createStory')
>>>>>>> ce207627e7c391c57e03746ac09f5aa66852e1d3

@app.route("/create", methods = ['GET', 'POST'])
def createStory():
	if request.method == "GET":
		return render_template('create.html')
	#if request.form['button'] == "Create":
	#	story.newStory(request.form['title'])
	#	return redirect(url_for('home'))


    
if __name__ == '__main__':
    app.run()
    app.debug = True
