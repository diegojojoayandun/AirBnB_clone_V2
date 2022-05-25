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
def task_100(id=None):
    """ Task 100 Function """
    list_states = storage.all(State)
    list_amenities = storage.all(Amenity)
    list_places = storage.all(Place)
    list_users = storage.all(User)
    return(render_template("100-hbnb.html", list_states=list_states,
                           list_amenities=list_amenities,
                           list_places=list_places,
                           list_users=list_users))

@app.teardown_appcontext
def storage_close(self):
    """
    Teardown_appcontext close
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
