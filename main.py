from flask import Flask, jsonify

app = Flask("API")

@app.route("/")
def mainPoint():
  respond = {"message"}