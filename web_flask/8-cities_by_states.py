#!/usr/bin/python3
"""
Task8 - script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """routes cities_by_states: display a render HTML page"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def storage_close(self):
    """
    teardown close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
