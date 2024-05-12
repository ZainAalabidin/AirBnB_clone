#!/usr/bin/python3
""" review module include Review class """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class inherit from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
