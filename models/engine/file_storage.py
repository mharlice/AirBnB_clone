#!/usr/bin/python3
"""Defines a FileStorage Class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """A class to create storage files from"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        obj: the object to set in
        """
        if obj:
            key = '.'.join([obj.__class__.__name__, obj.id])
            self.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dic, file)

    def reload(self):
        """
        deserializes the JSON file to __objects if file exists ;
        otherwise, do nothing.
        """
        file = self.__file_path
        if os.path.exists(file) and os.path.isfile(file):
            with open(file, "r") as f:
                dic = json.load(f)
                for key, value in dic.items():
                    # eval the 'class' key of <value> and initialize a new obj.
                    # this line of code calls the BaseModel __init__ method
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
