from flask import Flask
from flask import render_template
from flask import request
from flask import url_for,redirect,flash
import mongo

app = Flask(__name__)
app.secret_key = 'super_secret'

m = mongo.mongo()
#selStory =''

@app.route("/", methods=['GET','POST'])
def default():
    if request.method=='GET':
        stories = mongo.mongo.getStories(m)
        return render_template("default.html", stories=stories)
    else:
#        s = str(request.form['story'])
        ns = str(request.form['newStory'])
    
    b = request.form['button']
    if b=='Choose Story':
        return render_template("default.html")
    elif b == "Create Story":
        if not ns:
            return redirect(url_for('default'))
        else:
            mongo.mongo.newStory(m,ns)
            return redirect(url_for('default'))


        

if __name__ == "__main__":
    app.debug = True
    app.run()
