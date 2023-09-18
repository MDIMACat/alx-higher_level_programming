#!/usr/bin/python3
"""Class Base"""
import json


class Base:
    """Implemention a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        empty_list = '[]'
        new_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return empty_list

        if list_dictionaries:
            new_list = json.dumps(list_dictionaries)
            return new_list

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        obj_dict = {}
        obj_list = []

        if list_objs is None:
            return []

        class_name = cls.__name__

        filename = "{}.json".format(class_name)

        if list_objs is not None:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                obj_list.append(obj_dict)

        with open(filename, "w") as file:
            file.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        new_list = []

        if json_string:
            new_list = json.loads(json_string)

            return new_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""

        if cls.__name__ == "Rectangle":
            instance = cls(5, 2)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = None

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            return []

        instances = []
        for item in data:
            instance = cls.create(**item)
            instances.append(instance)

        return instances
