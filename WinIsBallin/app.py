from flask import Flask
from flsk import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
