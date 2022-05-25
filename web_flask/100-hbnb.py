#!/usr/bin/python3
"""
Task 12. HBNB is alive!
"""

from flask import Flask, render_template
from models import *
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """
    Route /hbnb
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    cities = storage.all(City)
    places = storage.all(Place)

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, cities=cities, places=places)


@app.teardown_appcontext
def storage_close(self):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
