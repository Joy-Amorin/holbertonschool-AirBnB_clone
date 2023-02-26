#!/usr/bin/python3
""" Module doc"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Class doc"""
    def __init__(self, *args, **kwargs):
        """__init__ doc"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    date_t = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, date_t))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return str"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """generate a dictionary representation of an instance"""
        dic = self.__dict__.copy()
        dic.update({"__class__": self.__class__.__name__,
                    "created_at": self.created_at.isoformat(),
                     "updated_at": self.updated_at.isoformat()})
        return dic
