#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == "db")
            else object):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") != 'db':
        name = ""

        @property
        def cities(self):
            """getter method, returns list de City objs"""
            city_list = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
    else:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
