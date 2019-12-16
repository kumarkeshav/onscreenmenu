from flask import Flask, render_template
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")
import csv
import datetime

#Menu to be displayed
menu = []
meal = "Closed"
PATH = 'resources/'

@app.route("/")
def hello():
    return "Hello World v2!"
    #return render_template("index.html")


def getTimebasedMenuFile():
    now = datetime.datetime.today()
    breakfast_start = now.replace(hour=9, minute=00, second=0)
    breakfast_end = now.replace(hour=12, minute=29, second=59)

    lunch_start = now.replace(hour=12, minute=30, second=0)
    lunch_end = now.replace(hour=14, minute=59, second=59)

    snacks_start = now.replace(hour=15, minute=00, second=0)
    snacks_end = now.replace(hour=19, minute=29, second=59)

    dinner_start = now.replace(hour=19, minute=30, second=0)
    dinner_end = now.replace(hour=22, minute=59, second=59)

    if now > breakfast_start and now < breakfast_end:
        return "breakfast.csv"
    if now > lunch_start and now < lunch_end:
        return "lunch.csv"
    if now > snacks_start and now < snacks_end:
        return "snacks.csv"  # /Users/sanyamgupta/PycharmProjects/onscreenmenu/resources/snacks.csv
    if now > dinner_start and now < dinner_end:
        return "dinner.csv"
    else:
        return "closed.csv"

@app.route("/display")
def display():
    fileName = getTimebasedMenuFile()
    fileName = fileName if fileName else "menu.csv"

    file = open(PATH + fileName, "r")
    reader = csv.reader(file)
    menu = list(reader)
    file.close()

    meal = fileName.split(".csv")[0].upper()
        
    return render_template("display.html", menu=menu, meal = meal)

@app.route("/configure", methods=["GET"])
def configure():
    return "Hello World v3!"
    #render_template("configure.html")
    
@app.route("/save_config", methods=["POST"])
def save_config():
    render_template("display.html")

app.run(host = '0.0.0.0', port = '5000', debug = 'True')
