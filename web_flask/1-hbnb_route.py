#!/usr/bin/python3
"""
Task 1. HBNB - starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    display "Hello HBNB!"
    """
    return '{}'.format("Hello HBN")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    display "HBNB"
    """
    return '{}'.format("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
