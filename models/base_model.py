#!/usr/bin/python3
"""
Module: base_model
This module defines the Base Model class for other classes.
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    base model with unique identifier and timestamped creation/update times.
    """

    def __init__(self, *args, **kwargs):
        """
        new instance with a unique id, creation time, and update time.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        changes updated_at attribute to current time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts object attributes to dict. for JSON.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns string rep of object class name, unique id, and attri.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
