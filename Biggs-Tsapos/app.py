from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect, flash,session
from flask import *
import util
app = Flask(__name__)
currentStory = ''


@app.route('/')
def start():
    return redirect(url_for('home'))

@app.route("/home/",methods=['GET','POST'])
def home():
    global currentStory
    if request.method=='GET':
        return render_template('home.html',count=util.numStories(),firstlines=util.getFirstLines())
    else:
        if request.form.has_key('reader'):
            currentStory=request.form['storychooser']
            print currentStory
            return redirect(url_for('page'))
        else:
             name=request.form['storystarter']
             util.addStory(name)
             return redirect(url_for('home'))

@app.route("/page/",methods=['GET','POST'])
def page():
    global currentStory
    if request.method=='GET':
        return render_template('page.html',Title=currentStory,restOfLines=util.getLines(currentStory))
    else:
        if request.form.has_key('submit'):
            newLine=request.form['newLineBox']
            util.addLine(newLine,currentStory)
            return redirect(url_for('page'))
        else:
            return redirect(url_for('home'))
       
if __name__ == '__main__':
    app.debug = True
    app.run()


