from crypt import methods
from flask import Flask, render_template, request
import db

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0",port=3000)
    