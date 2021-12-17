"""A simple flask web app"""
from flask import Flask, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/article1.html")
def article1():
    return render_template("article1.html")

@app.route("/article2.html")
def article2():
    return render_template("article2.html")

@app.route("/article3.html")
def article3():
    return render_template("article3.html")

@app.route("/article4.html")
def article4():
    return render_template("article4.html")

@app.route("/past.html")
def past():
    return render_template("past.html")

@app.route("/future.html")
def future():
    return render_template("future.html")

