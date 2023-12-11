#!/usr/bin/python3
"""Defines a City Class"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """A class to create City objects from"""
    state_id = ""
    name = ""
