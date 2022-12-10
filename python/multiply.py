
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/multiply", methods=["POST"])
def subtract():
    return jsonify({"data" : str(float(request.form["num1"]) * float(request.form["num2"]))})


if __name__ == "__main__":
    app.run(port=3000)