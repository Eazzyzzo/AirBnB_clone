#!/usr/bin/python3
"""
filestorage class module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON fil
    e and deserializes JSON file to instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                if cls_name == 'BaseModel':
                    self.__objects[key] = BaseModel(**value)
                elif cls_name == 'User':
                    self.__objects[key] = User(**value)
                elif cls_name == 'State':
                    self.__objects[key] = State(**value)
                elif cls_name == 'City':
                    self.__objects[key] = City(**value)
                elif cls_name == 'Amenity':
                    self.__objects[key] = Amenity(**value)
                elif cls_name == 'Place':
                    self.__objects[key] = Place(**value)
                elif cls_name == 'Review':
                    self.__objects[key] = Review(**value)
                # Add other class checks as needed
        except FileNotFoundError:
            pass
# Ensure globals dictionary contains all classes


globals().update({
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
})
