# coding=utf-8

from models.models_utils.player_manager import PlayerManager
from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from controllers.controller import Controller
from views.menus.players_menu import PlayersMenu
from views.forms.new_player_form import NewPlayerForm


class PlayerCtrl(Controller):
    """
    Controller class for Player
    """

    def __init__(self):
        self.menu = PlayersMenu()
        self.not_asked_properties = ['identifier']

    def add_player(self) -> Player:
        """
        this method creates a new player entry in the registry.
        """
        new_player_dict = NewPlayerForm().add_new()
        new_player = sf.factories[Player].create(**new_player_dict)
        return new_player

    def search_by_id(self, search) -> list:  # voir player manager : search_one_player
        """
        This method lists the player instances matching the given input (id)
        """
        results = sf.factories[Player].search(search)
        found_players_list = []
        for identifier in results:
            player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
            found_players_list.append(player_obj)
        ordered_by_id = sorted(found_players_list, key=lambda x: x.identifier)
        return ordered_by_id

    def sort_by_last_name(self) -> list:
        """
        This method returns a list of all players in the registry sorted by last name
        """
        players_list = PlayerManager().list_registered_players()
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    def sort_by_ranking(self) -> list:
        """
        This method returns a list of all players in the registry sorted by ranking
        """
        players_list = PlayerManager().list_registered_players()
        sorted_by_ranking = sorted(players_list, key=lambda x: x.ranking, reverse=True)
        return sorted_by_ranking
