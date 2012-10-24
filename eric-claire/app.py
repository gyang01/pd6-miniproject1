from flask import Flask, render_template
from flask import request
import database

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def home():
    if request.method == "GET":
        database.connect()
        titles = database.list_stories()
        return render_template("home.html",titles=titles)


if __name__ == "__main__":
    app.debug=True
    app.run()
