from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
from flask import session, escape

import databasing

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/", methods=['GET', 'POST'])
def start():
    if request.method=="GET":
        return render_template("default.html")
    else:
        story = request.form['story']
        newStory = request.form['newStory']

        button=request.form['button']
        if button=='go' or button =='create':
            return redirect(url_for('addLine'))
            
