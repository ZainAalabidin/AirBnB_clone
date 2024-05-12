#!/usr/bin/python3
""" city module have City class """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherit from BaseModel class """
    state_id = ""
    name = ""
