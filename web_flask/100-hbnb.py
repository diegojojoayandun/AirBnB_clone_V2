#!/usr/bin/python3
""" Task 100: script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def task_100():
    """
    Routes /hbnb
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    return(render_template("100-hbnb.html", states=states, amenities=amenities,
                           places=places, users=users))

@app.teardown_appcontext
def storage_close(self):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
