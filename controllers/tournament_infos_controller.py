# coding=utf-8
from datetime import datetime
from typing import Union
from uuid import UUID

from models.match import Match
from utils import split_even_list, lists_to_association_dict
from models.models_utils.player_manager import PlayerManager
from models.models_utils.supermanager import super_manager as sm
from models.player import Player
from models.round import Round
from controllers.controller import Controller
from controllers import tournaments_controller, list_tournaments_controller
from views.forms.new_match_form import NewMatchForm
from views.forms.new_round_form import NewRoundForm
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, tournament=None, players_results=None):
        if players_results is None:
            players_results = {}
        self.menu = TournamentInfosMenu(tournament)
        self.data = tournament
        self.players_results = players_results

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
    def sort_players_by_result(self) -> Union[list, str]:
        """
        This method lists all the players of a given tournament by result
        """
        if self.players_results == {}:
            return self.players_results
        else:
            player_obj_result_dict = {}
            for identifier in self.players_results:
                player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
                player_obj_result_dict[player_obj] = self.players_results[identifier]
            return sorted(player_obj_result_dict.items(), key=lambda x: x[1], reverse=True)  # on a l'identifier_str, pas le Player_obj

    def display_rounds_and_matches(self) -> list:
        """
        This method lists all the rounds of a given tournament
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
        self.generate_round_1_matchups()
        # while len(tournament.rounds_list) < tournament.rounds:
        #     self.add_players_scores()

        tournament_controller.run()

    def select_tournament(self):  # à rediger !

        self.data = list_tournaments_controller.ListTournamentsCtrl().select_one()
        round_1 = self.generate_round_1_matchups()
        self.get_round1_results(round_1)
        self.sort_players_by_result()
        self.generate_next_round_matchups()

        # self.get_next_round_results(self.players_results)
        # while len(self.data.rounds_list) < self.data.rounds:
        #    self.add_players_scores()

        TournamentInfosCtrl(self.data).run()

    def generate_round_1_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        # ROUND 1
        sorted_by_ranking = self.sort_tournament_players_by_ranking()
        lower_ranking_players_list, upper_ranking_players_list = split_even_list(sorted_by_ranking)
        round_couples = lists_to_association_dict(lower_ranking_players_list, upper_ranking_players_list)
        # return round_couples
        # on joue
        # on créé le round et on entre les resultats des matchs
        round_dict = NewRoundForm(self.data).add_new()
        _round = Round(**round_dict)
        for key in round_couples:
            player1_id = PlayerManager().from_player_obj_to_identifier_str(key)
            player2_id = PlayerManager().from_player_obj_to_identifier_str(round_couples[key])
            match_dict = NewMatchForm(self.data, player1_id, player2_id).add_new()
            match = Match(**match_dict)
            _round.matches.append(match)
        return _round

        # on recupère les points du Round 1
    def get_round1_results(self, _round: Round) -> dict:
        for match in _round.matches:
            self.players_results[match.player1_id_pod] = match.player1_score_pod
            self.players_results[match.player2_id_pod] = match.player2_score_pod
        return self.players_results  # -> dict(id:score)
        # il faut les stocker quelque part d'accessible ensuite pour pouvoir ajouter les points round apres round!

    def generate_next_round_matchups(self):
        player_results = self.players_results
        print(player_results)

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

    def list_tournament_players(self):
        tournament_players = []
        for uuid in self.data.identifiers_list:
            player_obj = PlayerManager().from_identifier_to_player_obj(uuid)
            tournament_players.append(player_obj)
        return tournament_players

    def add_players_scores(self):
        """
        This method enables to count the players points after a round
        and calculate the scores and ranking inside the tournament
        """
        pass