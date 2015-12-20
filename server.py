from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
from flask import abort
from flask import make_response
from flask import redirect

import os
import sys


#=====[ Sets up directories  ]=====
base_dir = os.path.split(os.path.realpath(__file__))[0]
static_dir = os.path.join(base_dir, 'static')

#=====[ Initializes app  ]=====
app = Flask(__name__, static_folder=static_dir)

#====[ Routes to home screen where user enters screen name  ]=====
@app.route("/")
def home():
	return 'hi Moco!'
	#return render_template("index.html.jinja2",tweeters=2)

if __name__ == "__main__":
	app.run()