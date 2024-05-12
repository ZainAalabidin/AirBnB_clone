#!/usr/bin/python3
""" module for FileStorage class. """

import datetime
import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances
    
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        opjCname = obj.__class__.__name__
        k = "{}.{}".format(opjCname, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dict, file)
    

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                obj_d = json.load(file)
                for key, value in obj_d.items():
                    cls_name = value['__class__']
                    obj_class = getattr(models, cls_name)  # Get class dynamically
                    obj = obj_class(**value)  # Instantiate object
                    self.__objects[key] = obj
        except Exception:
            pass

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str}}
        return attributes
