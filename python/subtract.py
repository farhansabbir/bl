
from flask import Flask, jsonify, request
import db
import datetime

app = Flask(__name__)

@app.route("/subtract", methods=["POST"])
def subtract():
    db.client.get_collection("data").insert_one({ str(datetime.datetime.now()) : {"/subtract": str(float(request.form["num1"]) - float(request.form["num2"]))}})
    return jsonify({"data" : str(float(request.form["num1"]) - float(request.form["num2"]))})


if __name__ == "__main__":
    app.run("0.0.0.0",port=3000)