from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")

def helloWorld():
    return "hello world"

if(__name__ == "_main_"):
    app.run(debug = True)