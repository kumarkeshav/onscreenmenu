from flask import Flask, render_template
app = Flask(__name__, instance_relative_config=False, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    #return "Hello World!"
    """Landing Page"""
    return render_template('/index.html', title = "Lame Site")

app.run(host='0.0.0.0', port=80, debug=True)