# coding=utf-8
from typing import Union

from models.models_utils import data
from models.models_utils.player_manager import PlayerManager
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from controllers.controller import Controller
from views.menus.players_menu import PlayersMenu
from views.forms.new_player_form import NewPlayerForm


class PlayersCtrl(Controller):
    """
    Controller class for Player
    """

    def __init__(self):
        self.menu = PlayersMenu()

    @staticmethod
    def add_player() -> Player:
        """
        this method creates a new player entry in the registry.
        """
        new_player_dict = NewPlayerForm().add_new()
        new_player = sm.managers[Player].create(**new_player_dict)
        data.save()
        return new_player

    def update_player_ranking(self, search: str) -> Union[list, Player]:
        """
        This method enables to manually update the ranking of a given player
        """
        self.menu.header_player_search()
        result = PlayerManager().search_one(search)
        if isinstance(result, list):
            return result
        elif isinstance(result, Player):
            new_ranking = NewPlayerForm().ask_ranking()
            result.ranking = new_ranking
            return result
        else:
            raise AttributeError

    @staticmethod
    def search_by_id(search: str) -> list:
        """
        This method lists the player instances matching the given input (id)
        """
        results = sm.managers[Player].search(search)
        found_players_list = []
        for identifier in results:
            player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
            found_players_list.append(player_obj)
        ordered_by_id = sorted(found_players_list, key=lambda x: x.identifier)
        return ordered_by_id

    @staticmethod
    def sort_by_last_name() -> list:
        """
        This method returns a list of all players in the registry sorted by last name
        """
        players_list = PlayerManager().list_registered_players()
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    @staticmethod
    def sort_by_ranking() -> list:
        """
        This method returns a list of all players in the registry sorted by ranking
        """
        players_list = PlayerManager().list_registered_players()
        sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        return sorted_by_ranking
