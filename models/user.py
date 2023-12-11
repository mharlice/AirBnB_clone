#!/usr/bin/python3
"""Defines a User Class"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """A class to create User objects from"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
