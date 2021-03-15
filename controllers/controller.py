# coding=utf-8

# si besoin
# supprimer si pas utile au final

import re

from constants import PLAYER_PROPERTIES, TOURNAMENT_PROPERTIES, EMPTY_SEARCH_STRINGS


# from .player_controller import PlayerCreator
# from .tournament_controller import TournamentCreator

from models.player import Player
from models.tournament import Tournament

from typing import Any


class Creator:
    """
    The Creator class is set as a common/factorized Class that enable to instantiate any type of object from a dict

    """
    def __init__(self, obj_type):
        self.registry = {}
        self.obj_type = obj_type

    def create(self, **params):
        obj = self.obj_type(**params)  # on créé l'instance
        identifier = obj.identifier  # on recupère l'identifier
        if identifier not in self.registry:  # on ajoute l'instance au registre
            self.registry[identifier] = obj
            return obj

    def search(self, identifier: str) -> Any: # on cherche l'ID et si on ne le trouve pas ValueError: l'ID n'existe pas (à améliorer pour avoir une recherche intelligente)
        if identifier in self.registry:
            return self.registry[identifier]
        raise ValueError(identifier)


def get_obj_type(_obj_dict): # pas utile pour le moment mais je garde pour l'instant
    """
    This method gets a dict as input and defines the type of object to create through the provided keys
    It then forwards the creation task to the right concrete Creator
    """
    properties_from_dict = []
    for key in _obj_dict:
        properties_from_dict.append(key)
    if properties_from_dict == PLAYER_PROPERTIES:
        print('New Player !')
        obj_type = Player
        return obj_type
    elif properties_from_dict == TOURNAMENT_PROPERTIES:
        print('New Tournament !')
        obj_type = Tournament
        return obj_type
    else:
        raise AttributeError(f'No object found for this dict!')


# on donne un uuid ou une partie de l'uuid, il doit renvoyer les Players correspondants
def get_by_id(search): # à travailler et mettre dans Creator : search
    """
    This method enables to get one or more Player instance(s) from their identifier
    It excludes empty searches.
    """
    registry = Creator.player_registry  # string de 4 attributs, la recherche doit etre améliorée !
    results = {}
    for key in registry:
        for search_match in re.finditer(search, key):
            if registry[key].identifier_pod not in results:
                results[key] = registry[key]
        if search in EMPTY_SEARCH_STRINGS:
            results = {}
    return results



