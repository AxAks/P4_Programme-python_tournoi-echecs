# coding=utf-8

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.player_manager import list_registered_players
from models.player import Player
from models.tournament import Tournament
from controllers.controller import Controller
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, selected_tournament):
        self.menu = TournamentInfosMenu()
        self.selected_tournament = selected_tournament

    # à rediger !
    def sort_players_by_last_name(self) -> list:  # voir comment utiliser serialize() ici
        """
        This function lists all the players of a given tournament by last name
        """
        """
        This method returns a list of all players in the registry sorted by last name
        """
        players_list = []
        for identifier in self.selected_tournament.identifier_list:
            players_list.append(sf.factories[Player].search(identifier))
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    def sort_players_by_result(self) -> list:  # voir comment utiliser serialize() ici
        """
        This function lists all the players of a given tournament by result
        """
        pass

    def display_rounds(self) -> list:  # voir comment utiliser serialize() ici
        """
        This function lists all the rounds of a given tournament
        """
        pass

    def display_matches(self) -> list:  # voir comment utiliser serialize() ici
        """
        This function lists all the matches of a given tournament
        """
        pass



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
    def add_match(self) -> None:  # est ce qu'une méthode est utile ici ? plutot dans controller Tournament je pense
        """
        This getter enables to add the information of a Match to the list of matches of the Round Object
        """
        pass