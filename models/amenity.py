#!/usr/bin/python3
"""Defines an Amenity Class"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class to create Amenity objects from"""
    name = ""
