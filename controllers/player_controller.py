# coding=utf-8

from models.player import Player
from models.models_utils.superfactory import super_factory as sf
"""
Controller file for Player
"""

"""
Temp : Just for me !
Controller : link between Models (Classes) and Views
-  models updates
plusieurs fichiers controller à écrire : scinder
"""


def sort_by_last_name():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
    return sorted_by_last_name


def sort_by_ranking():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)
    sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
    return sorted_by_ranking


def search_by_id(search):
    """
    This function lists the player instances matching the given input (id)
    """
    results = sf.factories[Player].search(search)
    found_players_list = []
    for uuid in results:
        player_obj = sf.factories[Player].registry[uuid]
        found_players_list.append(player_obj)
    return found_players_list



