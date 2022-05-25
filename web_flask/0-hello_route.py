#!/usr/bin/python3
"""
Task 0. Hello Flask!  starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    Display "Hello HBNB!"
    """
    return '{}'.format("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
