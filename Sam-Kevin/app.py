from flask import *

#import util

app = Flask(__name__)
app.secret_key = 'blah1orblah2'


@app.route("/")
def start():
    return redirect(url_for('login'))

@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        return redirect(url_for('home'))


@app.route("/home/",methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template("home.html")
    else:
        button=request.form['button']
        if button == 'Back':
            session.pop('user',None)
            return redirect('/login/')

if __name__=="__main__":
    app.debug=True
    app.run()
