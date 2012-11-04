from flask import Flask 
from flask import request, make_response
from flask import render_template
from flask import url_for,redirect,flash, escape
import mongo

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method=="GET":
		return render_template("homepage.html", stories = mongo.getAllTitles())
	if request.method=="POST":
		button=request.form["button"]
		if button=='Submit':
			name=request.form['name']
			mongo.addstory(name)
			return render_template("homepage.html", stories = mongo.getAllTitles())
                elif(button=='Go'): 
                        name=str(request.form['name'])
                        return render_template("addtostory.html", comments = mongo.getStory(name))
                
                        
                       
	
@app.route("/", methods=['GET', 'POST'])
def addtostory():
           if request.method=="POST":
                   button= request.form['button']
                   if button=="save":
                        line = str(request.form["comments"])
                        name = str(request.form["name"])
                        mongo.addLine(name, line)
                        return render_template("addtostory.html", name = name, comments = mongo.getStory(name))
                   if button=="cancel":
                           return redirect(url_for(home))
           
if __name__=="__main__":
        app.debug = True
	app.run(port=5000)
