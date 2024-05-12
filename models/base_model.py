#!/usr/bin/python3
""" this script for base model """

import uuid
from datetime import datetime
import models


class BaseModel:
    """my BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initialized instance attributes.

        Args:
            - args: list of arguments (unused).
            - kwargs: key/value pairs of attributes.
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert the string to a datetime object before formatting
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return official string"""
        type_name = type(self).__name__
        return "[{}] ({}) {}".format(type_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts instance attributes to dictionary format."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
