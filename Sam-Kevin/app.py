from flask import *

#import mongo

global Story
app = Flask(__name__)
app.secret_key = 'blah1orblah2'

global story
@app.route("/")
def start():
    return redirect(url_for('login'))

@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method=='GET':
#        story = util.getStories;
        return render_template("login.html")#,story=story)
    else:
        button=request.form['button']
        if button == "GO":
# story = Textfield[story]
            return redirect('/home/'+story)


@app.route("/home/<story>/",methods=['GET','POST'])
def home(story):
    if request.method=='GET':
#        story=getStory();
        return render_template("home.html")#,story=story)
    else:
        button=request.form['button']
        if button == 'Back':
            session.pop('user',None)
            return redirect('/login/')

if __name__=="__main__":
    app.debug=True
    app.run()
