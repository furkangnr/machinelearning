from flask import Flask, jsonify, request
import numpy as np


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello World"


@app.route("/<username>")
def my_func(username):
    return f"Hello World, This is {username}!"


@app.route("/prediction")
def func1():
    arr = np.linspace(0, 100, 15)
    return jsonify([i for i in arr])


@app.route("/devs", methods=["GET", "POST"])
def func2():
    if request.method == "GET":
        return str(100)
    else:
        return str(0)


if __name__ == "__main__":
    app.run("127.0.0.1", debug=True, port=8080)
