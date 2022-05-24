#!/usr/bin/python3
"""
Task 10: script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def task_10_1():
    """ Task 10 Function """
    list_states = storage.all(State)
    return(render_template("9-states.html", states=list_states, id=None))


@app.route("/states/<id>", strict_slashes=False)
def task_10_2(id):
    """ Task 10 Function """
    list_states = storage.all(State)
    for state in list_states.values():
        if state.id == str(id):
            return(render_template("9-states.html", states=state))
    return(render_template("9-states.html", no_state=None))


@app.teardown_appcontext
def call_storage_close(exception):
    """ close the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
