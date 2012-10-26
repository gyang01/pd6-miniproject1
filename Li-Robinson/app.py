from flask import Flask,render_template,request,redirect,url_for
import util

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    util.auth()
    if request.method == 'GET':
        titles = util.get_story_titles()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["button"]
        if button == "Go":
            storyname = str(request.form["story_menu"])
            #print storyname #the above does indeed work
            if storyname:
                lines = util.get_lines(storyname)
            else:
                lines = []
            return render_template("home.html",storyname=storyname,lines=lines)
        
        elif button == "Delete Story":
            storyname = str(request.form["story_menu"])
            if storyname:
                util.del_story(storyname)
            titles = util.get_story_titles()
            return render_template("home.html",titles=titles)

        elif button == "Back":
             titles = util.get_story_titles()
             return render_template("home.html",titles=titles)
        
        elif button == "Create":
            storyname = request.form["new_story"]
            if storyname:
                util.add_story(storyname)
            titles = util.get_story_titles()
            return render_template("home.html",titles=titles)
            #return redirect(url_for(home)) #no this should NOT be a redirect

        else: # button is a story name
            storyname = button
            newline = request.form["next_line"]
            if storyname and newline:
                util.add_line(storyname,newline)
            lines = util.get_lines(storyname)
            return render_template("home.html",storyname=storyname,lines=lines)

#@app.route("/story",methods=['GET','POST'])
#def story(storyname):
#    util.auth()
#    if request.method == 'GET':
#        pass
#    else:
#        pass


if __name__ == "__main__":
    app.debug = True
    app.run()
    #app.run(port=5000)
