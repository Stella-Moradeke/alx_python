#!/usr/bin/python3
"""
models/base.py:
This module defines the Base class, which serves as the base class for all other classes in the project.
"""

class Base:
    """
    Base class for managing the id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects