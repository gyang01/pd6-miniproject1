from flask import Flask
from flask import request, make_response
from flask import render_template
import db
from flask import url_for,redirect,flash, escape

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="GET":
        return render_template("webage.html")
    else:
        button=request.form['button']
        if button=='Create!':
            title=request.form['ntitle']
            db.add_story(title)
            return redirect(url_for(home))
        elif:
            if button=='Read!':
                otitle=request.form['otitle']
                resp=make_response(render_template("webpage.html"))
                resp.set_cookie('title', otitle)
                return redirect(url_for(story))
            return redirect(url_for(home))
            
if __name__=="__main__":
    app.debug=True
    app.run()
