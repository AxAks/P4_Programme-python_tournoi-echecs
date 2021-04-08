# coding=utf-8

import re

from typing import Any

from constants import EMPTY_SEARCH_STRINGS


class Factory:
    """
    The Factory class is set as a common/factorized Class that enable to instantiate any type of object from a dict.
    This Class creates specific Factories based on the object's type
    The instances are registered in a registry and can be searched for.
    """

    def __init__(self, obj_type):
        self.registry = {}
        self.obj_type = obj_type

    def create(self, **params) -> Any:
        """
        This method creates new objects through the specific factory
        and adds them to a registry if the identifier is not already registered
        """
        obj = self.obj_type(**params)
        identifier = obj.identifier
        self.registry[identifier] = obj
        return obj

    def search(self, search: str) -> Any:
        results = {}
        for key in self.registry:
            for search_match in re.finditer(search, str(key)):
                if self.registry[key].identifier not in results:
                    results[key] = self.registry[key]
            if search in EMPTY_SEARCH_STRINGS:
                results = {}
        return results