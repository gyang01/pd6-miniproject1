from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("home.html,title=title")

@app.route("/story",methods=["GET", "POST"])
def story():
    return redner_template("display
