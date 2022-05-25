#!/usr/bin/python3
"""
Task 3. Python is cool! starts a Flask web application
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
    return '{}'.format("Hello HBN")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display “C ” followed by the value of the text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text='is cool'):
    """
    Display “Python ”, followed by the value of the text variable
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
