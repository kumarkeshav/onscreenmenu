from flask import Flask, render_template
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
import csv

#Menu to be displayed
menu = []

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
    return render_template("display.html", menu=menu)

@app.route("/configure", methods=["GET"])
def configure():
    return "Hello World v3!"
    #render_template("configure.html")
    
@app.route("/save_config", methods=["POST"])
def save_config():
    render_template("display.html")

app.run(host = '0.0.0.0', port = '5000', debug = 'True')
