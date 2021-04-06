# coding=utf-8
from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from controllers.controller import Controller
from views.forms.add_player_form import NewPlayerForm
from views.menus.player_menu import PlayerMenu

"""
Controller file for Player
"""


class PlayerCtrl(Controller):
    def __init__(self):
        self.menu = PlayerMenu()

    def add_player(self) -> Player:
        """
        this method creates a new player entry in the registry.
        """
        new_player_dict = NewPlayerForm().add_new_player()
        new_player = sf.factories[Player].create(**new_player_dict)
        return new_player

    def sort_by_last_name(self) -> list:
        """
        This method returns a list of all players in the registry sorted by last name
        """
        players_list = []
        for uuid in sf.factories[Player].registry:
            player_obj = sf.factories[Player].registry[uuid]
            players_list.append(player_obj)
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    def sort_by_ranking(self) -> list:
        """
        This method returns a lsit of all players in the registry sorted by ranking
        """
        players_list = []
        for uuid in sf.factories[Player].registry:
            player_obj = sf.factories[Player].registry[uuid]
            players_list.append(player_obj)
        sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        return sorted_by_ranking

    def search_by_id(self, search):
        """
        This method lists the player instances matching the given input (id)
        """
        results = sf.factories[Player].search(search)
        found_players_list = []
        for uuid in results:
            player_obj = sf.factories[Player].registry[uuid]
            found_players_list.append(player_obj)
        return found_players_list
