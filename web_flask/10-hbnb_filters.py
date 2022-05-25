#!/usr/bin/python3
"""
Task 11. HBNB filters
"""

from flask import Flask, render_template
from models import *
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Route /hbnb_filters
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def storage_close(self):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
