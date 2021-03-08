# coding=utf-8

from constants import PLAYER_PROPERTIES, TOURNAMENT_PROPERTIES, ROUND_PROPERTIES, MATCH_PROPERTIES

from controllers.controller_match import MatchCreator
from controllers.controller_round import RoundCreator
from controllers.player_controller import PlayerCreator
from controllers.tournament_controller import TournamentCreator


# si besoin
# supprimer si pas utile au final
from models.player import Player
from models.tournament import Tournament


# class Creator:
"""
The Creator class is set as a common/factorized Parent Class for child Objects
à continuer ....
"""
def create_object(self, _obj_dict, properties_from_dict):
    """
    This method calls the method in chargereator
    """
    creator = self._get_creator(properties_from_dict)
    return creator(_obj_dict)

def _get_creator(_obj_dict):
    """
    This method gets a dict as input and defines the type of object to create through the provided keys
    It then forwards the creation task to the right concrete Creator
    """
    properties_from_dict = []
    for key in _obj_dict:
        properties_from_dict.append(key)
    if properties_from_dict == PLAYER_PROPERTIES:
        print('New Player !')
        return PlayerCreator.create_player(_obj_dict)
    elif properties_from_dict == TOURNAMENT_PROPERTIES:
        print('New Tournament !')
        return TournamentCreator.create_tournament(_obj_dict)
    elif properties_from_dict == ROUND_PROPERTIES:
        print('New Round !')
        return RoundCreator.create_round(_obj_dict)
    elif properties_from_dict == MATCH_PROPERTIES:
        print('New Match !')
        return MatchCreator.create_match(_obj_dict)
    else:
        raise AttributeError(f'No object found for this dict!')


def create_player(player_dict): # à voir !
    """
    This method creates Player instances
    and hold a registry of the created players.
    à continuer ...
    """
    new_player = Player(**player_dict)
    Player.registry[
    new_player.identifier_pod] = new_player  # registry = {} : key = Player.identifier, value = instance
    return new_player

def create_tournament(tournament_dict):  #  à voir !
    """
    This method receives dicts from the abstract Creator for Tournament instances to be created
    and hold a registry of the created Tournaments.
    à continuer ...
    """
    # return new Tournament instance
    new_tournament = Tournament(**tournament_dict)
    Tournament.registry[
        new_tournament.identifier] = new_tournament  # registry = {} : key = Tournamment.identifier, value = instance
    print('New Tournament Created and stored !')
    return new_tournament

# on donne les infos d'un tournoi , il doit renvoyer le Tournament
def get_tournament(*args):
    """
    This method enables to get a Tournament instance from its identifier attributes : Name, Location or Dates.
    """
    registry = Tournament.registry # en l'état, il faut que les trois membres du tuple soient présents et dans l'ordre
    for tuple_id in registry:
        if args in registry:
            return registry[tuple_id]