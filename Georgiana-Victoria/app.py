from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect
import db

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
	db.auth()
	if request.method == 'GET':
		titles=db.getTitles()
		return render_template("home.html",titles=titles)
	else:
		button=request.form["button"]
		if button == "Create!":
			newname=str(request.form["newtitle"])
			db.add_story(newname)
			titles=db.getTitles()
			return redirect(url_for('home'))
		else:
			if button=='Read!':
				selected=request.form.get("otitle","")
				titles=db.getTitles()
				return redirect(url_for('home'))
			return redirect(url_for('home'))
	#titles=db.getTitles()
	#return render_template("home.html",titles=titles)
            
if __name__=="__main__":
    app.debug=True
    app.run()
