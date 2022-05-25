#!/usr/bin/python3
"""
Task 6. Odd or even? starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Dsiplay "HBNB"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_is_fun(text):
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


@app.route('/number/<int:n>', strict_slashes=False)
def int_number(n):
    """
    Display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_number_template(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_or_odd(n):
    """
    Display a HTML page only if n is an integer
    and shows if it is even or odd.
    """
    if n % 2 == 0:
        is_odd_or_even = 'even'
    else:
        is_odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           is_odd_or_even=is_odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
