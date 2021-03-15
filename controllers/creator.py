# coding=utf-8

import re

from typing import Any

from constants import EMPTY_SEARCH_STRINGS


class Creator:
    """
    The Creator class is set as a common/factorized Class that enable to instantiate any type of object from a dict.
    This Class creates specific Creators based on the object's type
    """
    def __init__(self, obj_type):
        self.registry = {}
        self.obj_type = obj_type

    def create(self, **params):
        """
        This method creates new objects through the specific creator and adds them to a registry
        """
        obj = self.obj_type(**params)  # on créé l'instance
        identifier = obj.identifier  # on recupère l'identifier
        if identifier not in self.registry:  # on ajoute l'instance au registre
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
