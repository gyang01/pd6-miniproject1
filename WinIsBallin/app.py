from flask import Flask
from flask import render_template
from flask import request

import story

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html', stuff="stuff")
    if request.form['button'] == "Create New Story":
	return redirect(url_for('createStory')

@app.route("/createStory", methods=['POST'])
def createStory:
	if request.method == "GET":
		return render_template('createStory.html')
	if request.form['button'] == "Create":
		story.newStory(request.form['title'])
		return redirect(url_for('home')


    
if __name__ == '__main__':
    app.run()
    app.debug = True
