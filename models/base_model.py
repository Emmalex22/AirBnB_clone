#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():
    """This is a basemodel which serves as a parent class for all classes in this project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def save(self):
        """A method to save and update users data"""
        self.updated_at = datetime.now()
        
    def __str__(self):
        """returns the string representation of a class instance"""
        return f"[self.__class__.__name__]" {self.id} {self.__dict__}
    def to_dict(self):
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict['__created_at__'] = self.created_at.isoforrmat
        mydict['__updated_at__'] = self.updated_at.isoformat
        return mydict