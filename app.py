from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates", static_folder="static")
import csv
import datetime

#Menu to be displayed
menu = []
meal = "Closed"
PATH = 'resources/'
cod = 0
codv = None
codnv = None

@app.route("/")
def hello():
    return "Hello World v2!"
    #return render_template("index.html")


def getTimebasedMenuFile():
    cod = 0
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
        cod = 0
        return "breakfast.csv", cod
    if now > lunch_start and now < lunch_end:
        cod = 1
        return "lunch.csv", cod
    if now > snacks_start and now < snacks_end:
        cod = 0
        return "snacks.csv", cod  # /Users/sanyamgupta/PycharmProjects/onscreenmenu/resources/snacks.csv
    if now > dinner_start and now < dinner_end:
        cod = 1
        return "dinner.csv", cod
    else:
        cod = 0
        return "closed.csv", cod

def getMenuandMeal():
    fileName, cod = getTimebasedMenuFile()
    fileName = fileName if fileName else "menu.csv"

    file = open(PATH + fileName, "r")
    reader = csv.reader(file)
    menu = list(reader)
    file.close()
    #cod = 1
    meal = fileName.split(".csv")[0].upper()
    return menu, meal, cod

def updateCOD(codv2, codnv2):
    codv = codv2
    codnv = codnv2
    return codv, codnv

@app.route("/display")
def display():
    menu, meal, cod = getMenuandMeal()
    return render_template("display.html", menu=menu, meal=meal, cod=cod, codv=codv, codnv=codnv)

@app.route("/configure", methods=["POST"])
def configure():
    menu, meal, cod = getMenuandMeal()
    global codv
    codv = request.form.get("codv")
    global codnv
    codnv = request.form.get("codnv")
    #codv, codnv = updateCOD(codv1, codnv1)
    #return codv
    return render_template("display.html", menu=menu, meal=meal, cod=cod, codv=codv, codnv=codnv)
    #return render_template("nav.html", name=name, name1=name1)
    
@app.route("/save_config")
def save_config():
    return render_template("configure.html")
    #return "Hello World v3!"

app.run(host = '0.0.0.0', port = '5000', debug = 'True')
