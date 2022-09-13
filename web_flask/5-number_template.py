#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/, strict_slashes=False")
def hello_hbnb():
    """module hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    return "C " + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_Python(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
