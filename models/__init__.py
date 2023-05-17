#!/usr/bin/python3
"""The __init__ method for models directory"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


storage = FileStorage()
storage.reload()

classes = {"BaseModel": BaseModel}

# , "User": User, "State": State, "City": City,
#  "Amenity": Amenity, "Place": Place,"Review": Review
