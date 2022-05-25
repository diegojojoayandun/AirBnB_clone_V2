#!/usr/bin/python3
"""
Task 9. Cities by states
"""

from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Routes /cities_by_states
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def storage_close(self):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
