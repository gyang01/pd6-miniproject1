from flask import Flask
from flask import request, make_response
from flask import render_template
import whoostory, unicodedata
from flask import url_for,redirect,flash, session, escape, request

app = Flask(__name__)
app.secret_key = 'paulmawhyhaveyouforsakenme'

@app.route("/",methods=['GET','POST'])
def home():
	if request.method == "GET":
		return render_template("webpage.html", storylist=whoostory.getalltitles())
	else:
		button = request.form['button']
		if button=="DROP THE BASS!(Deletes all stories)" :
			whoostory.dropstories()
			return redirect(url_for('home'))
		elif button=="...and make it!":
			whoostory.addstory(request.form['nustory'])
			return redirect(url_for('home'))
		elif button=="Drop it!":
			whoostory.dropspecstory(request.form['chosenstory'])
			return redirect(url_for('home'))
		return redirect(url_for('story', name = request.form['chosenstory']))
		
#huh
@app.route("/story/<name>",methods = ["GET", "POST"])
def story(name = None):
	if request.method == "GET":
		if whoostory.exists(name):
			return render_template("story.html", story=name, lines = whoostory.getstorytext(name))
		else:
			return redirect(url_for('home'))
	else:
		button = request.form['button']
		if button=="Back to Homepage":
			return redirect(url_for('home'))
		else:
			a= request.form['yay']
			if len(a) >0:
				whoostory.addline(name,a)
			return redirect(url_for('story', name = name))

#	else:

'''#Users can only rate one person at a time - scroll choice option
@app.route("/titleused",methods = ["GET", "POST"])
def rate():
	if request.method == "GET":
		return render_template("titleused.html", q=q, group=utils.get_mygroup(user)) 
	elif 'user' not in session:
		flash('Please log in')
		return redirect(url_for('login'))
	else:
		button=request.form['button']
		if button=='Save':
			myemail=unicodedata.normalize('NFKD',session['user']).encode('ascii','ignore')
			yoemail=request.form["ratee"] 
			rates=[]
			i=0
			for i in range(4):
				rates.append(request.form[str(i)])
			print rates
			utils.saveRes(myemail,yoemail,rates)
			return redirect(url_for('rate'))
		elif button=='Cancel':
			return redirect(url_for('home'))
		return redirect(url_for('rate'))
'''
if __name__=="__main__":
	app.debug=True
	app.run(port=5000)
	
