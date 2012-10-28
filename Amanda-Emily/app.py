from flask import Flask 
from flask import request, make_response
from flask import render_template
from flask import url_for,redirect,flash, escape
import mongo #not sure if this is right, might be import db

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method=="GET":
		return render_template("homepage.html")
	else: #what to do if the user submits a new story
		button=request.form['button']
		if button=='Submit':
			title=request.form['name']
			db.add_story(title)
			return redirect(url_for(home))
		elif: #what to do if the user picks a story in progress
			if button=='Go':
			title=request.form['name'] #not sure if I should refer to this as title/will this cause any conflicts?
			return redirect(url_for((story))
		return redirect(url_for(home)) 
                       
	
	
if __name__=="__main__":
	app.debug=True
	app.run()