from flask import Flask, render_template
from flask import request, redirect
import database

app = Flask(__name__)
global current_story

@app.route("/",methods=["GET", "POST"])
def home():
    global current_story
    database.connect()
    if request.method == "GET":
        titles = database.list_stories()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Create":
            newtitle = request.form.get("newStory")
            current_story = database.add_new_story(newtitle)
#add_new_story(title) returns the what it added because it might differ from
#newtitle (eg, "" turn into "Untitled" and duplicates get numbered
            return redirect("/"+current_story) #each story gets its own URL
        elif button == "View story":
            title = str(request.form["view_one"]) #dropdown menu named view_one
            current_story = title #need to keep track of the story
            return redirect("/"+current_story)
        elif button == "Drop story":
            title = request.form["view_one"] #same as View story, but instead
            database.remove_one(title)       #returns the homepage
            titles = database.list_stories() 
            return render_template("home.html",titles=titles) 

@app.route("/"+"<storyname>",methods=["GET","POST"])
def story(storyname):
    global current_story
    database.connect()
    if request.method == "GET": #this is true when you use redirect
        title = current_story #current_story is saved when you press View story
        lines = database.get_lines(title)
        return render_template("home.html",title=title,lines=lines)
    else:
        button = request.form["button"]
        if button == "Add line":
            newLine = request.form.get("newLine") #text box named newLine
            title = current_story #gotten from when you pressed View story
            database.add_sentence(title,newLine)
            lines = database.get_lines(title)
            return render_template("home.html",title=title,lines=lines)
        elif button == "Back":
            return redirect("/")


if __name__ == "__main__":
    app.debut=True
    app.run()
