#!/usr/bin/python3
"""Defines an Amenity Class"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class to create Amenity objects from"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        super().__init__(args, kwargs)
