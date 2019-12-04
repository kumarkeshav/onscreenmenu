from flask import Flask
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")

@app.route("/")
def hello():
    return "Hello World v2!"
    #return render_template("index.html")

@app.route("/menu")
def menu_display():
    #return "Hello World v2!"
    return render_template("menu.html")

app.run(host = '0.0.0.0', port = '5000', debug = 'True')