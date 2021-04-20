# coding=utf-8
from datetime import datetime
from uuid import UUID

from controllers import list_tournaments_controller
from controllers.players_controller import PlayerCtrl
from models.models_utils.player_manager import PlayerManager
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

    def add_round_and_matches(self) -> Round:
        """
        This method enables to add a Round and the associasted Matches to the Tournament Object
        """
        new_round_dict = NewRoundForm(self.data).add_new()
        new_round = Round(**new_round_dict)
        self.data.rounds_list.append(new_round)
        return new_round

    def add_start_time(self) -> datetime:  # doit etre renseigné automatiquement en fait ! # à reflechir...
        """
        This method automatically sets the start time of the Round Object
        """
        return datetime.now()

    def add_end_time(self) -> datetime:  # doit etre renseigné automatiquement en fait ! # à reflechir
        """
        This method automatically sets the end time of the Round Object
        """
        return datetime.now()






    def add_new_tournament(self):
        new_tournament = list_tournaments_controller.TournamentCtrl().add_tournament()
        tournament_controller = TournamentInfosCtrl(new_tournament)
        tournament = tournament_controller.data
        while len(tournament.rounds_list) != tournament.rounds:
            self.generate_matchups()
            NewRoundForm.add_new()
            NewMatchForm.add_new()
            self.add_players_scores()

        tournament_controller.run()

    def select_tournament(self):
        selected_tournament = list_tournaments_controller.ListTournamentsCtrl().select_one()
        tournament_controller = TournamentInfosCtrl(selected_tournament)
        tournament = tournament_controller.data
        while len(tournament.rounds_list) != tournament.rounds:
            self.generate_matchups(tournament)
            NewRoundForm.add_new()
            NewMatchForm.add_new()
            self.add_players_scores()

        tournament_controller.run()

    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        sorted_by_ranking = self.sort_tournament_players_by_ranking()

        middle_index = len(sorted_by_ranking) // 2
        upper_ranking_players_list = sorted_by_ranking[:middle_index]
        lower_ranking_players_list = sorted_by_ranking[middle_index:]




        pass

    def sort_tournament_players_by_ranking(self):
        tournament_players = []
        players_identifiers = self.data.identifiers_list
        for identifier in players_identifiers:
            player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
            tournament_players.append(player_obj)
        sorted_by_ranking = sorted(tournament_players, key=lambda x: x.ranking, reverse=True)
        return sorted_by_ranking

    def add_players_scores(self):
        """
        This method enables to count the players points after a round
        and calculate the scores and ranking inside the tournament
        """
        pass