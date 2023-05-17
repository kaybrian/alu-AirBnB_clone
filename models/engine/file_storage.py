#!/usr/bin/python3
"""
convert the dictionary representation to a JSON string.
"""
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances:

    Attributes:
        __file_path: path to the JSON file
        __objects: dictionary
    """
    __file_path = "file.json"
    # Stores all objects by <class name>.id
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            """Check if the object exits then save it"""
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
