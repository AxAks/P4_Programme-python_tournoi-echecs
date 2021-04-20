# coding=utf-8
from datetime import datetime
from uuid import UUID

from models.match import Match
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from controllers.controller import Controller
from models.round import Round
from views.forms.new_match_form import NewMatchForm
from views.forms.new_round_form import NewRoundForm
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, tournament):
        self.menu = TournamentInfosMenu(tournament)
        self.data = tournament

    def sort_players_by_last_name(self) -> list:
        """
        This method lists all the players of a given tournament by last name
        """
        players_list = []
        for identifier in self.data.identifiers_list:
            player_obj = sm.managers[Player].search(identifier)
            players_list.append(player_obj[UUID(identifier)])
        sorted_by_last_name = sorted(players_list, key=lambda x: x.last_name)
        return sorted_by_last_name

    # à rediger !
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
    #  -> Tournament = self.data donc Round = self.data.rounds_list
    #  -> dans le controller TournamentInfos !? à voir
    #  Le Match doit etre identifié dans Round (dans la liste de matchs)
    #  Round.matches
    # comment j'encastre le tout

    # pour ajouter un round ou des rounds à Tournament
    def add_round(self) -> Round:  # voir si utile à un moment
        """
        This method enables to add a Round to the Tournament Object
        """
        new_round_dict = NewRoundForm(self.data).add_new()
        new_round = Round(**new_round_dict)
        self.data.rounds_list.append(new_round)
        return new_round

    # pour ajouter un match à Round
    def add_match_to_round(self) -> None:
        """
        This method enables to add the informations of a Match to the list of matches of the Round Object
        """
        pass

    def add_start_time(self) -> datetime:  # doit etre renseigné automatiquement en fait !
        """
        This method autoamtically sets the start time of the Round Object
        """
        return datetime.now()

    def add_end_time(self) -> datetime:  # doit etre renseigné automatiquement en fait !
        """
        This method autoamtically sets the end time of the Round Object
        """
        return datetime.now()
