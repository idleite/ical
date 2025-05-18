from flask import Flask
from app import main
app = Flask(__name__)

@app.route("/<classes>/<name>")
def classes(classes, name):
    return main(classes, name)
@app.route("/healthz")
def health():
    return "OK - Good"
