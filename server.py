from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<x>")
def second(x):
    x_box = 8
    return render_template("second.html", ybox=int(x), xbox=int(x_box))


@app.route("/<x>/<y>")
def third(x, y):
    return render_template("third.html", x_coor=int(x), y_coor=int(y))
