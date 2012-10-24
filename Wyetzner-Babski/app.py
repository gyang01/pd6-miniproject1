from flask import Flask
from flask import render_template
from flask import request
from flask import url_for,redirect,flash
import mongo

app = Flask(__name__)
app.secret_key = 'super_secret'

@app.route("/", methods=['GET','POST'])
def default():
    if request.method=='GET':
        return render_template("default.html")
    if request.method=='POST':
        button=request.form['button']
        if button=='Choose Story':
            return render_template("default.html")
        if button=='Create Story':
            mongo.newstory(str(request.form["newstory"]))
            return render_template("default.html")
        

if __name__ == "__main__":
    app.debug = True
    app.run()
