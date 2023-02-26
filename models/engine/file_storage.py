#!/usr/bin/python3
"""Module """
import os
import json


class FileStorage:
    """class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj"""

        FileStorage.__objects[f"{obj.__class__.__name__} {obj.id}"] = obj

    def save(self):
        """serializes"""
        with open(FileStorage.__file_path, "w") as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dct()
                json.dump(obj_dict, f)

    def reload (self):
        """deserializes the JSON fie"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dict_j = json.loads(f)
                for key, value in dict_j.items():
                    FileStorage.__objects[key] = BaseModel.new(**value)
        except FileNotFoundError:
            pass
