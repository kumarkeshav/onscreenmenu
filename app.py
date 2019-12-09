from flask import Flask, render_template
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
import csv
from datetime import datetime

#Menu to be displayed
menu = []
meal = "Closed"

@app.route("/")
def hello():
    return "Hello World v2!"
    #return render_template("index.html")

@app.route("/display")
def display():
    file = open("menu.csv", "r")
    reader = csv.reader(file)
    menu = list(reader)
    file.close()
    
    now = datetime.now()
    if int(now.strftime("%H")) > 1 and int(now.strftime("%H")) < 22:
        meal = "Breakfast"
        
    return render_template("display.html", menu=menu, meal = meal)

@app.route("/configure", methods=["GET"])
def configure():
    return "Hello World v3!"
    #render_template("configure.html")
    
@app.route("/save_config", methods=["POST"])
def save_config():
    render_template("display.html")

app.run(host = '0.0.0.0', port = '5000', debug = 'True')
