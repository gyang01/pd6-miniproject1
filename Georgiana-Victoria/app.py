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
		#elif button=='Read!':
		#	selected=request.form.get("otitle","")
		#	titles=db.getTitles()
		#	return redirect(url_for('home')) #story.html TBC
		elif button=='Drop Story':
			selected=request.form.get("drop","")
			db.remove_story(selected)
			return redirect(url_for('home'))
		return redirect(url_for('home'))
	return redirect(url_for('home'))

@app.route("/story/<s>",methods=['GET','POST'])
def story(s="default story"):
	db.auth()
	if request.method=='GET':
		lines=db.getLines(s)
		print lines
		return render_template("story.html",lines=lines,title=s)
	else:
		button=request.form['button']
		if button=="Add":
			nline=str(request.form.get("line",""))
			print nline
			db.add_line(s, nline)
			print "test"
			#lines=db.getLines(s)
			return redirect(url_for('story', s=s))
		elif button=="Back":
			return redirect(url_for("home"))
	lines=db.getLines(s)
	return render_template("story.html",lines=lines,title=s)
	


if __name__=="__main__":
	app.debug=True
	app.run()
	
	
