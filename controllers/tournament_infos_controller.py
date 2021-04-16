# coding=utf-8
from uuid import UUID

from models.models_utils.superfactory import super_factory as sf
from models.player import Player
from controllers.controller import Controller
from views.forms.new_match_form import NewMatchForm
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, tournament):
        self.menu = TournamentInfosMenu(tournament)
        self.data = tournament

    # à rediger !
    def sort_players_by_last_name(self) -> list:
        """
        This method lists all the players of a given tournament by last name
        """
        players_list = []
        for identifier in self.data.identifiers_list:
            player_obj = sf.factories[Player].search(identifier)
            players_list.append(player_obj[UUID(identifier)])
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    def sort_players_by_result(self) -> list:
        """
        This function lists all the players of a given tournament by result
        """
        pass

    def display_rounds_and_matches(self) -> list:
        """
        This function lists all the rounds of a given tournament
        """
        return self.data.rounds_list

    #  Comment gère t-on la reference à Tournament dans Round ? à voir -> Round n'existe pas hors de Tournament
    #-> dans le controller Tournament !? à voir

    # Le Round doit etre identifié dans Tournament ( dans la liste de Rounds)
    # // Le Match doit etre identifié dans Round ( dans la liste de matchs)

    # pour ajouter un round ou des rounds à Tournament
    def add_round(self) -> None:  # voir si utile à un moment
        """
        This method enables to add the list of Matches of a Round to the Tournament Object
        """
        pass

    # pour ajouter un match à Round
    def add_match(self, tournament) -> None:
        """
        This method enables to add the information of a Match to the list of matches of the Round Object
        """
        pass
