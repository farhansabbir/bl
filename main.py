from crypt import methods
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    return str(float(request.form["num1"]) + float(request.form["num2"]))

@app.route("/subtract", methods=["POST"])
def subtract():
    return str(float(request.form["num1"]) - float(request.form["num2"]))

@app.route("/divide", methods=["POST"])
def divide():
    return str(float(request.form["num1"]) / float(request.form["num2"]))

@app.route("/multiply", methods=["POST"])
def multiply():
    return str(float(request.form["num1"]) * float(request.form["num2"]))


if __name__ == "__main__":
    app.run(debug=True, port=3000)