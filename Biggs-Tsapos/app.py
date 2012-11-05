from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect, flash,session
from flask import *
import util
import time
app = Flask(__name__)
currentStory = ''
filler = []


@app.route('/')
def start():
    return redirect(url_for('home'))

@app.route("/home/",methods=['GET','POST'])
def home():
    global currentStory
    global filler
    if request.method=='GET':
        tmp = filler
        filler = []
        return render_template('home.html',count=util.numStories(),firstlines=util.getFirstLines(),checker=tmp)
    else:
        if request.form.has_key('reader'):
            currentStory=request.form['storychooser']
            return redirect(url_for('page'))
        if request.form.has_key('clear'):
            util.clearStories()
            return redirect(url_for('home'))
        if request.form.has_key('submit'):
            name=request.form['storystarter']
            if name.replace(' ','') != '':
                util.addStory(name)
                currentStory = name
                return redirect(url_for('page'))
            else:
                filler = ["filler","otherstuff"]
                return redirect(url_for('home'))            

@app.route("/page/",methods=['GET','POST'])
def page():
    global currentStory
    global timex
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


