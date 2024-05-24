#!/usr/bin/python3
import uuid
from datetime import datetime
import json


myuser = {}

class BaseModel():
    """This is the parent class for all classes in this project"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """A method to save and update users data"""
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of a class instance"""
        return f"[{self.__class__.__name__}] ({self.id})({self.__dict__})"

    def to_dict(self):
        mydict = self.__dict__.copy()
        mydict['__class__'] = self.__class__.__name__
        mydict["id"] = self.id
        mydict["created_at"] = self.created_at.isoformat
        mydict['updated_at'] = self.updated_at.isoformat
        return mydict

class User(BaseModel):
    """A user class that inherits from the basemodel"""
    def __init__(self, name):
        """initializes the user class"""
        super().__init__()
        self.name = name

    def do_create(self, line):
        arg = line.split()
        if len(arg) != 2 or arg[0].lower() != "create":
            print("Ivalid syntax: use create <name>")
            return
        name = arg[1]
        new_user = User(name)
        myuser[new_user.id] = new_user
        print(f"New user created with user id: {new_user.id} and name: {new_user.name}")
class Storage(BaseModel):
    """"""