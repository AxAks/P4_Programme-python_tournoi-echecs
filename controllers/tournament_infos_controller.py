# coding=utf-8
from datetime import datetime
from typing import Union
from uuid import UUID


from models.models_utils.player_manager import PlayerManager
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from models.round import Round
from controllers.controller import Controller
from controllers import tournaments_controller, list_tournaments_controller
from views.forms.new_round_form import NewRoundForm
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, tournament=None):
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

    def add_round_and_matches(self) -> Union[list[Round], None]:
        """
        This method enables to add a Round and the associasted Matches to the Tournament Object
        """
        if self.data.rounds_list == self.data.rounds:
            return None
        new_round_dict = NewRoundForm(self.data).add_new()
        new_round = Round(**new_round_dict)
        self.data.rounds_list.append(new_round)
        return new_round

    def add_start_time(self) -> datetime:  # datetime.now() quand on le créé, ou on entre le moemnt où les joueurs ont commencé à jouer
        """
        This method automatically sets the start time of the Round Object
        """
        return datetime.now()

    def add_end_time(self) -> datetime:  # doit etre renseigné automatiquement en fait à la fin de saisie ! # à reflechir
        """
        This method automatically sets the end time of the Round Object
        """
        return datetime.now()





    def add_new_tournament(self):  # à rediger !
        new_tournament = tournaments_controller.TournamentCtrl().add_tournament()
        tournament_controller = TournamentInfosCtrl(new_tournament)
        tournament = tournament_controller.data
        while len(tournament.rounds_list) < tournament.rounds:
            self.generate_round_1_matchups()
            NewRoundForm(self.data).add_new()
            self.add_players_scores()

        tournament_controller.run()

    def select_tournament(self):  # à rediger !
        self.data = list_tournaments_controller.ListTournamentsCtrl().select_one()
        while len(self.data.rounds_list) < self.data.rounds:
            self.generate_round_1_matchups()
            NewRoundForm(self.data).add_new()
            self.add_players_scores()

        TournamentInfosCtrl(self.data).run()

    def generate_round_1_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        # ROUND 1
        sorted_by_ranking = self.sort_tournament_players_by_ranking()
        lower_ranking_players_list, upper_ranking_players_list = self.split_list(sorted_by_ranking)
        round_couples = self.lists_to_dict_association(lower_ranking_players_list, upper_ranking_players_list)
        return round_couples
        # on joue
        # on entre les resultats, comment ??
        for key, value in couples_dict:
            player1_id = key.identifier
            player2_id = value.identifier
            NewRoundForm(self.data).add_new() # ca va changer !
        # on recupère les points

        pass

    def lists_to_dict_association(self, list1, list2) -> dict[Player:Player]:
        """
        This method compares two lists
        and associates their items though their indices in respective list
        """
        return {list2[i]: list1[i] for i in range(len(list1))}


    def split_list(self, sorted_by_ranking):
        """
        This method splits a list in the midlle into two sub-lists
        """
        middle_index = len(sorted_by_ranking) // 2
        # on fait des sous listes
        upper_ranking_players_list = sorted_by_ranking[:middle_index]
        lower_ranking_players_list = sorted_by_ranking[middle_index:]
        return lower_ranking_players_list, upper_ranking_players_list

    def sort_tournament_players_by_ranking(self) -> list[Player]:
        """
        This method sorts the players of the tournament by ranking from high to low
        """
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