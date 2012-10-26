#!/usr/bin/python
from flask import Flask, render_template, session, url_for, redirect, request, escape
import os 
import storinator
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route("/", methods = ["GET", "POST"])
def home():
    
    
 if request.method == "GET":
  return render_template("homeminiproj.html")
 else:
        storinator.con()
        storyarray= storinator.getstories()
        button = request.form["button"]
        if button == "create" and len(str(request.form["storyname"])) > 0:
            storinator.addstory(str(request.form["storyname"]))
            return render_template("homeminiproj.html")
        if button == "go":
            storypick = str(request.form["storypick"])
            return redirect(url_for("storypage"))

@app.route("/", methods = ["GET", "POST"])
def storypage():
 if request.method == "GET":
    return render_template("storypage.html")
 else:
     button2 = request.form["button2"]
     storycont = storinator.get_story(storypick)
    if button2 == "Add":
        newline = str(request.form["newline"])
        storinator.addcontent(storypick,newline)
        return render_template("storypage.html")
    if button2 == "Go Back":
        return redirect(url_for("home"))
            
        
if __name__ == "__main__":
	app.run(debug = True)        
        
        
