# coding=utf-8

# si besoin
# supprimer si pas utile au final

import re

from constants import PLAYER_PROPERTIES, TOURNAMENT_PROPERTIES, ROUND_PROPERTIES, MATCH_PROPERTIES, \
    EMPTY_SEARCH_STRINGS

from controllers.match_controller import MatchCreator
from controllers.round_controller import RoundCreator
from controllers.player_controller import PlayerCreator
# from controllers.tournament_controller import TournamentCreator

from models.player import Player
from models.tournament import Tournament


class Creator:
    """
    The Creator class is set as a common/factorized Parent Class for child Objects
    à continuer ....
    """
    player_registry = {}
    tournament_registry = {}

    def create(self, _obj_dict, properties_from_dict):
        """
        This method calls the method defining the right Creator for the provided dictionary
        """
        creator = self._get_creator(properties_from_dict)
        return creator(_obj_dict)

    def _get_creator(self, _obj_dict):
        """
        This method gets a dict as input and defines the type of object to create through the provided keys
        It then forwards the creation task to the right concrete Creator
        """
        properties_from_dict = []
        for key in _obj_dict:
            properties_from_dict.append(key)
        if properties_from_dict == PLAYER_PROPERTIES:
            print('New Player !')
            return PlayerCreator.create(_obj_dict)
        elif properties_from_dict == TOURNAMENT_PROPERTIES:
            print('New Tournament !')
            return TournamentCreator.create(_obj_dict)
        elif properties_from_dict == ROUND_PROPERTIES:
            print('New Round !')
            return RoundCreator.create(_obj_dict)
        elif properties_from_dict == MATCH_PROPERTIES:
            print('New Match !')
            return MatchCreator.create(_obj_dict)
        else:
            raise AttributeError(f'No object found for this dict!')


def create_player(player_dict): # à voir ! TEST
    """
    This method creates Player instances
    and hold a registry of the created players.
    à continuer ...
    """
    new_player = Player(**player_dict)
    Creator.player_registry[
    new_player.identifier_pod] = new_player  # registry = {} : key = Player.identifier, value = instance
    return new_player

# on donne un player_uuid, il doit renvoyer les Player correspondants
def get_by_id(search):
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
    """
    registry = Creator.player_registry
    if player_id in registry:
        return registry[player_id]
    """

def create_tournament(tournament_dict):  #  à voir ! TEST
    """
    This method receives dicts from the abstract Creator for Tournament instances to be created
    and hold a registry of the created Tournaments.
    à continuer ...
    """
    # return new Tournament instance
    new_tournament = Tournament(**tournament_dict)
    Creator.tournament_registry[
        new_tournament.identifier] = new_tournament  # registry = {} : key = Tournamment.identifier, value = instance
    print('New Tournament Created and stored !')
    return new_tournament

# on donne les infos d'un tournoi , il doit renvoyer les Tournaments correspondants
def get_tournament(search):
    """
    This method enables to get a Tournament instance from its identifier attributes : Name, Location or Dates.
    """
    registry = Creator.tournament_registry  # string de 4 attributs, la recherche doit etre améliorée !
    results = {}
    for key in registry:
        for search_match in re.finditer(search, key):
            if registry[key].identifier not in results:
                results[key] = registry[key]
        if search in EMPTY_SEARCH_STRINGS:
            results = {}
    return results

    results = {}
    for key in registry:
        for search_match in re.finditer(search, key):
            if registry[key].identifier_pod not in results:
                results[key] = registry[key]
    if search in ('', ' ', '-'):
        results = {}
    return results
