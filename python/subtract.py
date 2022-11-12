
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/subtract", methods=["POST"])
def subtract():
    return str(float(request.form["num1"]) - float(request.form["num2"]))


if __name__ == "__main__":
    app.run(port=3001)