<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask
import csv #lightweight database

>>>>>>> 4c414f7b4efa45e63668b11a2a304ca284aa2c76
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")

#Menu to be displayed
menu = []

@app.route("/")
<<<<<<< HEAD
def home():
    #return "Hello World!"
    """Landing Page"""
    return render_template('/index.html', title = "Lame Site")

app.run(host='0.0.0.0', port=80, debug=True)
=======
def hello():
    return "Hello World v2!"
    #return render_template("index.html")

@app.route("/display")
def display():
    return render_template("display.html")

@app.route("/configure", methods=["GET"])
def configure():
    render_template("configure.html")
    
@app.route("/save_configure", methods=["POST"])
def configure():
    render_template("display.html")

app.run(host = '0.0.0.0', port = '5000', debug = 'True')
>>>>>>> 4c414f7b4efa45e63668b11a2a304ca284aa2c76
