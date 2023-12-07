#!/usr/bin/python3
"""Defines a State Class"""
from models.base_model import BaseModel
from datetime import datetime
import uuid
import models


class State(BaseModel):
    """A class to create State objects from"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        super().__init__(args, kwargs)
