# coding=utf-8
import collections
from datetime import datetime
from typing import Union
from uuid import UUID

from models.match import Match
from models.tournament import Tournament
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

    # à adapter avec tournament et total_results à la place de round results
    def sort_players_by_result(self, tournament: Tournament) -> Union[list, str]:
        """
        This method lists all the players of a given tournament by result
        """
        if tournament.total_results == {}:
            return tournament.total_results
        else:
            player_obj_result_dict = {}
            for identifier in tournament.total_results:
                player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
                player_obj_result_dict[player_obj] = tournament.total_results[identifier]
            return sorted(player_obj_result_dict.items(), key=lambda x: x[1], reverse=True)

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
        self.add_players_points_to_tournament_totals(round_1)
        self.sort_players_by_result(self.data)
        self.generate_next_round_matchups(round_1)

        # self.get_next_round_results(_round)
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
            player1_id = key.identifier_pod
            player2_id = round_couples[key].identifier_pod
            match_dict = NewMatchForm(self.data, player1_id, player2_id).add_new()
            match = Match(**match_dict)
            _round.matches.append(match)
        self.data.rounds_list.append(_round)
        return _round

        # on recupère les points du Round 1
    def get_round1_results(self, _round: Round) -> dict:
        _round.results = {}
        for match in _round.matches:
            _round.results[match.player1_id_pod] = match.player1_score_pod
            _round.results[match.player2_id_pod] = match.player2_score_pod
        return _round.results  # -> dict(id:score)
        # Je veux acceder à l'attribut 'results' du Round en question pour ajouter le dict des resultats
        # il faut les stocker les resultats par player dans le Round

    def add_players_points_to_tournament_totals(self, _round: Round) -> dict:
        if self.data.total_results == {}:
            total_pts_by_player = _round.results
        else:
            #  pas bon !! je veux : prendre les values pour chaque player_id (key) dans les dicts et les additionner
            counter = collections.Counter()
            total_pts_by_player = [self.data.total_results, _round.results]
            for player in total_pts_by_player:
                counter.update(player)
        return total_pts_by_player
        # pour pouvoir ajouter les points round apres round au total_results de tournament

    def generate_next_round_matchups(self, _round: Round):
        player_results = _round.results
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