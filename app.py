from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/to-ukraine")
def to_ukraine():
    return "<p>No war please!</p>"

@app.route("/home")
def home():
    return render_template('home.html')
