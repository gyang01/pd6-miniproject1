from flask import Flask
from flask import render_template
from flask import request
import utils

app = Flask(__name__)


@approute("/", methods=['GET','POST']
def default():
    if request.method=="GET":
        return render_template("default.html")
