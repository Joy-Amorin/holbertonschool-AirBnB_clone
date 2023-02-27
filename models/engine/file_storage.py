#!/usr/bin/python3
"""Module """
import json
import os.path


class FileStorage:
    """class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets obj"""

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON fie"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                dict_j = json.loads(f.read())
            for key, value in dict_j.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
