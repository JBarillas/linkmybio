from flask import Flask, jsonify, render_template, request
import os, optparse, sys
app = Flask(__name__)


developer = os.getenv("Developer", "Juan Barillas")
environment = os.getenv("ENVIRONMENT", "development")

@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", mivariable=foo,developer=developer)

@app.route("/Academic Information")
def api_students():
    pass

@app.route("/Work Experience")
def falta():
    pass

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug = True
    print("local change")
    app.run(host="0.0.0.0", debug=debug)
