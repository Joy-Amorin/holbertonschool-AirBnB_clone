#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        dic_f = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(dic_f))

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dict_j = json.loads(f.read())
            for key, value in dict_j.items():
                if key.split(".")[0] == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
                if key.split(".")[0] == "User":
                    self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
