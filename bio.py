from flask import Flask, jsonify, render_template, request
import os, optparse, sys
app = Flask(__name__)


developer = os.getenv("Developer", "Juan Barillas")
environment = os.getenv("ENVIRONMENT", "development")

alumnos = {
    "Andrea Reyes": 19,
    "Katherine Garcia": 17,
    "Fabricio Juarez": 18,
    "Jean Mejicanos": 17,
    "Steven Wilson": 19,
    "Ian Jenatz": 19,
    "Anesbeth Maatens": 17,
    "Tirso Cordova": 20,
    "Abner Xocop": 21,
    "Andres Bolanos": 21,
    "Katherin Mazariegos": 19,
    "Daniel Hernandez": 20,
    "Maite de la Roca": 20,
    "Diego Quan": 22,
    "Fernando Gonzalez": 20,
    "Boris Rendon": 19,
    "Adriana Mundo": 20,
    "Alejandra Lemus": 19,
    "Juan Barillas": 21,
    "David Corzo": 19,
    "Giovanny Telon": 25
}

@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", mivariable=foo,developer=developer)

@app.route("/Alumnos")
def api_students():
    return jsonify(alumnos)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug = True
    print("local change")
    app.run(host="0.0.0.0", debug=debug)