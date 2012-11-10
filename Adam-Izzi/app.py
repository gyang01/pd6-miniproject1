from flask import Flask,render_template, url_for,redirect,request
import db

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def storynatorHome():
    global title
    if request.method=='GET':
         return render_template("storynatorHome.html", titles = db.getStories())
    if request.method=='POST':
        if request.form["button"]=="Select":
            title = str(request.form["storyPicked"])
            lines = db.getLines(title)
            #return render_template("storypage.html", title = title, lines = lines)
            return redirect(url_for("storypage"))
        if request.form["button"]=="Drop":
            db.dropStory(str(request.form["storyPicked"]))
            return render_template("storynatorHome.html", titles = db.getStories())
        if request.form["button"]=="Create":
            db.addStory(str(request.form["newTitle"]))
            return render_template("storynatorHome.html", titles = db.getStories())
        
@app.route("/story",methods=['GET','POST'])
def storypage():
    if request.method=='GET':
        lines = db.getLines(title)
        return render_template("storypage.html", title = title, lines = lines)
    if request.method=='POST':
        if request.form["button"] == "Save":
            line = str(request.form["newLine"])
            db.addLine(title, line)
            lines = db.getLines(title)
            return render_template("storypage.html", title = title, lines = lines)
        if request.form["button"] == "Home":
            return redirect(url_for("storynatorHome"))
        
if __name__ == '__main__':
    app.debug = True
    app.run()

