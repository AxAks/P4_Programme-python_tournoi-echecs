# coding=utf-8
import operator

from models.player import Player
from models.superfactory import super_factory as sf
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
        players_list.append(player_obj)# on a une liste d'objects
    sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
    return sorted_by_last_name



def sort_by_ranking():
    players_list = []
    for uuid in sf.factories[Player].registry:
        player_obj = sf.factories[Player].registry[uuid]
        players_list.append(player_obj)# on a une liste d'objects
    sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
    return sorted_by_ranking


def search_by_id():  # marche pas mauvais affichage
    _input = input('Enter a Player ID: ')
    return sf.factories[Player].search(_input)

