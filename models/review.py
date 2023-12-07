#!/usr/bin/python3
"""Defines a Review Class"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """A class to create Review objects from"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        super().__init__(args, kwargs)
