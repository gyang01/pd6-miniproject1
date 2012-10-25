from flask import Flask
from flask import render_template
from flask import request

import story

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html', stuff="stuff")
    else:
        button = request.form['button']
        if button == "Create New Story":
            return redirect(url_for('createStory'))
        elif button == "Contribute to Existing Story"
    

@app.route("/create", methods = ['GET', 'POST'])
def createStory():
    if request.method == "GET":
        return render_template('create.html')
    else:
        button = request.form['button']
        if button == "Create":
            story.newStory(request.form['title'])
            return redirect(url_for('home'))

@app.route("/stories", methods = ['GET', 'POST'])
def stories():
    if request.method == 'GET':
        db = story.db()
        titles = []
        for title in db.getStoryNames():
            titles.append()
        return render_template('stories.html', titles=titles) 
    else:
        button = request.form['button']
        if button  == "Select":
            return redirect(url_for('storyadd.html'))
            
@app.route("/storyadd", methods = ['GET', 'POST'])
def storyadd():
    if request.method == 'GET':
        
        
        
if __name__ == '__main__':
    app.run()
    app.debug = True
