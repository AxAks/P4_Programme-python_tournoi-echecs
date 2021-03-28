# coding=utf-8

from models.player import Player
from views.menus.player_menu import PlayerMenu
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


# pas utilisé pour le moment !
class PlayerController(Player, PlayerMenu):
    def __init__(self):
        super().__init__()


def search_by_id():
    return sf.factories[Player].search

