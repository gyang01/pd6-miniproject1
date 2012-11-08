from flask import Flask,render_template, url_for,redirect,request
import db

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    mydb=db.db()
    if request.method=='GET':
         return render_template("storynatorHome.html")
    else:
        if request.method=='POST':
            if request.form["button"]=="Create":
                mydb.addStory(str(request.form['title']))
                return render_template("storynatorHome.html", titles = db.getStories())
            if request.form["button"]=="Go":
                title = request.form(str(request.form['title']))
                return render_template("storypage.html", title = title, lines = db.getLines(title))
        
