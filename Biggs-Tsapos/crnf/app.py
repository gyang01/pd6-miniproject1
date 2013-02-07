from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect, flash,session
from flask import *
import util

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html',titles=util.getTitles())
    if request.method == 'POST':
        if request.form.has_key('add'):
            return redirect(url_for('addPiece'))

@app.route('/addpiece',methods=['POST','GET'])
def addPiece():
    if request.method == 'GET':
        return render_template('addpiece.html')
    else:
        if request.form.has_key('back'):
            return redirect(url_for('home'))
        if request.form.has_key('submit'):
            title = request.form['title']
            if 'anon' in request.form:
                author = 'Anonymous'
            else:
                author = request.form['author']
            work = request.form['work']
            if 'feedback' in request.form:
                feedback = True
            else:
                feedback = False
            util.addWork(author,work,title,feedback)
            return redirect(url_for('piece',author=author,title=title))

@app.route('/piece/<author>/<title>',methods=['POST','GET'])
def piece(author,title):
    if request.method == 'GET':
        info = util.getWork(title,author)
        info[2] = info[2].replace('\n','<br>')
        return render_template('piece.html',info=info)
    if request.method == 'POST':
        if request.form.has_key('back'):
            return redirect(url_for('home'))
        if request.form.has_key('submit'):
            comment = request.form['comment']
            commenter = request.form['commenter']
            if str(commenter).replace(' ','') == '':
                commenter = 'Anonymous'
            util.addComment(title,author,comment,commenter)
            return redirect(url_for('piece',author=author,title=title))

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port='6151')
