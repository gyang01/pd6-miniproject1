from flask import Flask
from flask import url_for,redirect,flash
from flask import session, escape
from flask import request
from flask import render_template
import databasing
from pymongo import connection
import util

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def begin():
    global story = ""
     if request.method=="GET":
        return render_template("home.html")
     if request.method=="POST":
         button = request.form["button"]
         if button == "Ok":
             story = str(request.form["stories"])
             return redirect(url_for("story"))
         if button == "Add":
             util.addstory(str(request.form["storyname"]))
             return render_template("home.html")
             

@app.route("/story", methods = ["GET", "POST"])
def story():
