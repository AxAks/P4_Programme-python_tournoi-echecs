# coding=utf-8

from controllers.controller import Controller
from models.tournament import Tournament
from views.menus.tournament_infos_menu import TournamentInfosMenu
from models.models_utils.superfactory import super_factory as sf

class TournamentInfosCtrl(Controller):
    def __init__(self):
        self.menu = TournamentInfosMenu()


    # à rediger !
    def sort_players_by_last_name(self):
        """
        This function lists all the players of a given tournament by last name
        """
        pass

    def sort_players_by_result(self):
        """
        This function lists all the players of a given tournament by result
        """
        pass

    def list_rounds(self):
        """
        This function lists all the rounds of a given tournament
        """
        pass

    def list_matches(self):
        """
        This function lists all the matches of a given tournament
        """
        pass



    #  Comment gère t-on la reference à Tournament dans Round ? à voir -> Round n'existe pas hors de Tournament
    #-> dans le controller Tournament !? à voir

    # Le Round doit etre identifié dans Tournament ( dans la liste de Rounds)
    # // Le Match doit etre identifié dans Round ( dans la liste de matchs)

    # pour ajouter un round ou des rounds à Tournament
    def add_round(self):  # voir si utile à un moment
        """
        This method enables to add the list of Matches of a Round to the Tournament Object
        """
        pass


    # pour ajouter un match à Round
    def add_match(self):  # est ce qu'une méthode est utile ici ? plutot dans controller Tournament je pense
        """
        This getter enables to add the information of a Match to the list of matches of the Round Object
        """
        pass