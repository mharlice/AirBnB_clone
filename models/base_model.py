#!/usr/bin/python3
"""Defines a BaseModel Class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """A class to create BaseModel objects from"""
    def __init__(self, *args, **kwargs):
        """Initializes the object"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs is not None and len(kwargs):
            for key in kwargs:
                if key not in ['__class__', 'created_at', 'updated_at']:
                    setattr(self, key, kwargs[key])
            for i in ['created_at', 'updated_at']:
                if i in kwargs:
                    setattr(self, i, datetime.fromisoformat(kwargs[i]))
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """Returns string representation of object"""
        return self.__str__()

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing attributes of the instance"""
        dic = self.__dict__.copy()
        dic.update({'__class__': self.__class__.__name__,
                    'created_at': self.created_at.isoformat(),
                    'updated_at': self.updated_at.isoformat()})
        return dic
