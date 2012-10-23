from flask import Flask,render_template,request,redirect,url_for
import util

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    util.auth()
    if request.method == 'GET':
        titles = util.get_story_titles()
        #print titles
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Go":
            
        elif button == "Create":
            storyname = request.form["new_story"]
            util.add_story(storyname)
            titles = util.get_story_titles()
            #print titles
            return render_template("home.html",titles=titles)

@app.route("/story",methods=['GET','POST'])
def story(storyname):
    util.auth()
    if request.method == 'GET':
        pass
    else:
        pass


if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(port=5000)
