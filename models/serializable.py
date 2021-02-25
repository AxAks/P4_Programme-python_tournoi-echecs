# coding=utf-8

from enum import Enum


class Serializable:
    """
    This class enables to serialize Python Objects to simple types handled by TinyDB
    It uses introspection to access the object's attributes and methods.
    """
    # def __init__(self): je vais le construire après

    def serialize(self,):
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict
