from crypt import methods
from pickle import GET
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    return str(float(request.form["num1"]) + float(request.form["num2"]))

if __name__ == "__main__":
    app.run(debug=True, port=3000)