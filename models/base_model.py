#!/usr/bin/python3
"""write class BaseModel"""

from datetime import datetime
import uuid


class BaseModel:

    id = str(uuid.uuid4())
    created_at = datetime.now()
    update_at = datetime.now()

    def __str__(self):
        """reurn str id, classname, __dict__"""
        return f"[{__class__.__name__}] {(self.id)} {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime """
        update_at = datetime.now
        return update_at

    def to_dict(self):
        dic = self.__dict__.copy()
        dic.update({"__class__": self.__class__.__name__,
                    "created_at": self.created_at.isoformat(),
                    "update_at": self.update_at.isoformat()})
        return dic
