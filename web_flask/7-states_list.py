#!/usr/bin/python3
"""
Task 8. List of states
"""

from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    route /states_list
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def storage_close(exception):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
