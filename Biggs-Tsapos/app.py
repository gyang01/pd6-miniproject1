from flask import Flask
from flask import render_template
from flask import request
from flask import url_for, redirect, flash,session
from flask import *
import util
app = Flask(__name__)

@app.route('/')
def home():
    

if __name__ == '__main__':
    app.debug = True
    app.run()
