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
        storinator.addstory(str(request.form["storyname"]))
        storyarray=[]

        for valjean in db.stories.find():
         storyarray.append(valjean['story'])

        #button = request.form["button"]

        
         

        #if button == "go":
         #   return render_template("storypage.html")
