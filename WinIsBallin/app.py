from flask import Flask
from flask import render_template
from flask import request

import story

app = Flask(__name__)



@app.route("/")
def home():
    if requst.method == "GET":
        return render_template('home.html', stuff="stuff")

if __name__ == '__main__':
    app.run()
    app.debug = True
