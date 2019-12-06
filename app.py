from flask import Flask, render_template
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")

#Menu to be displayed
menu = []

@app.route("/")
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
