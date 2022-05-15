#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from models.review import Review
import os


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        reviews = relationship("Review",
                              cascade="all, delete",
                              backref="places")

    else:

        @property
        def reviews(self):
            """returns the list of City instances with state_id"""
            reviews_list = []
            _reviews = models.storage.all(Review)
            for _review in _reviews.values():
                if self.id == _review.place_id:
                    reviews_list.append(_review)
            return reviews_list

