from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/to-ukraine")
def to_ukraine():
    return "<p>No war please!</p>"
