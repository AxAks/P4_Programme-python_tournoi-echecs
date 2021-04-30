# coding=utf-8
import collections
from datetime import datetime
from typing import Union, Any
from uuid import UUID

from models.models_utils import data
from models.models_utils.player_manager import PlayerManager
from models.models_utils.supermanager import super_manager as sm
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from controllers.controller import Controller
from controllers import list_tournaments_controller
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
        tournament_players = []
        for identifier in self.data.identifiers_list:
            player_obj = sm.managers[Player].search(identifier)
            tournament_players.append(player_obj[UUID(identifier)])
        sorted_by_last_name = sorted(tournament_players, key=lambda x: x.last_name)
        return sorted_by_last_name

    def sort_tournament_players_by_ranking(self) -> list[Player]:
        """
        This method sorts the players of the tournament by general ranking from high to low
        """
        tournament_players = []
        for identifier in self.data.identifiers_list:
            player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
            tournament_players.append(player_obj)
        sorted_by_ranking = sorted(tournament_players, key=lambda x: (x.ranking, x.last_name, x.first_name),
                                   reverse=True)
        return sorted_by_ranking

    def sort_players_by_result(self, tournament: Tournament) -> Union[list[Player], Any]:
        """
        This method sorts all the players of a given tournament by result
        from highest to lowest
        It also takes into account the general ranking of the players in case of tie result
        """
        if tournament.total_results == {}:
            return tournament.total_results
        else:
            player_obj_result_dict = {}
            for identifier in tournament.total_results:
                player_obj = PlayerManager().from_identifier_to_player_obj(identifier)
                player_obj_result_dict[player_obj] = tournament.total_results[identifier]
            sorted_by_results_ranking = sorted(player_obj_result_dict.items(),
                                               key=lambda x: (x[1], x[0].ranking), reverse=True)
            return sorted_by_results_ranking

    def display_rounds_couples(self) -> list[tuple]:
        """
        This method lists the generated player matchups for the different rounds of a given tournament
        """
        return self.data.rounds_couples   # pb de savegarde des tuples dans serialize pas géré par json !!

    def display_rounds_and_matches(self) -> list:
        """
        This method lists all the rounds of a given tournament
        """
        return self.data.rounds_list


    def add_start_time(self) -> datetime:
        """
        This method automatically sets the start time of the Round Object
        """
        return datetime.now()

    def add_end_time(self) -> datetime:
        """
        This method automatically sets the end time of the Round Object
        """
        return datetime.now()



    def add_new_tournament(self):  # à rediger !
        new_tournament = list_tournaments_controller.ListTournamentsCtrl().add_tournament()
        tournament_controller = TournamentInfosCtrl(new_tournament)
        tournament = tournament_controller.data
        matchups_round_1 = self.generate_round_matchups(is_first=True)
        round_1 = self.enter_new_round(matchups_round_1)
        self.get_round_results(round_1)
        self.add_players_points_to_tournament_totals(round_1)
        matchups_round_2 = self.generate_round_matchups()
        round_2 = self.enter_new_round(matchups_round_2)
        self.get_round_results(round_2)
        self.add_players_points_to_tournament_totals(round_2)

        # while len(tournament.rounds_list) < tournament.rounds:
        # PlayersMenu().update_player_ranking() # à la fin updater les ranking des players, mais ne pas appeler le PlayerMenu directement, passer par PlayerCtrl

        tournament_controller.run()

    def select_tournament(self):  # à rediger ! et pour les tester
        self.data = list_tournaments_controller.ListTournamentsCtrl().select_one()
        # si on tape un mauvais identifier tournament, ca pete !
        while len(self.data.rounds_list) < self.data.rounds:  # pour mettre fin au tournoi quand il n'y a plus de round a faire
            if len(self.data.rounds_list) == 0:
                matchups_next_round = self.generate_round_matchups(is_first=True)
            else:
                matchups_next_round = self.generate_round_matchups()
            next_round = self.enter_new_round(matchups_next_round)
            self.get_round_results(next_round)
            self.add_players_points_to_tournament_totals(next_round)
            data.save()

        # for identifier in self.data.identifiers_list:
        #     new_ranking = PlayersMenu().update_player_ranking() # à la fin updater les ranking des players, mais ne pas appeler le PlayerMenu directement, passer par PlayerCtrl
        TournamentInfosCtrl(self.data).run()

    def generate_round_matchups(self, is_first=False) -> Union[list[tuple], dict]:
        """
        This method generates the tournament match-ups between the Players for a new round.
        It takes into account the players general rankings and/or results in the tournament
        an whether it is the first round or another round
        """
        # It should also checks that the players have not already player together
        if is_first:
            sorted_players_obj = self.sort_tournament_players_by_ranking()
        else:
            sorted_players_results = self.sort_players_by_result(self.data)
            sorted_players_obj = [_tuple[0] for _tuple in sorted_players_results]
        round_couples = self.get_round_couples(sorted_players_obj)
        #  verifier vers ici dans self.data.rounds_couples si une association de joueurs est deja présente dans les rounds précédents (dans self.data.rounds_couples)
        self.data.rounds_couples.append(round_couples) #  enregistre les round_couples du nouveau round sur tournament pour pouvoir verifier si les joueurs ont déjà joué ensemble
        return round_couples

    def get_round_couples(self, sorted_players: Union[list, dict]) -> Union[list[Player], list[tuple], str]:
        if len(sorted_players) % 2 == 0:
            middle_index = len(sorted_players) // 2
            upper_ranking_players_list = sorted_players[middle_index:]
            lower_ranking_players_list = sorted_players[:middle_index]
        else:
            return 'This list does not have an even number of items'
        if len(upper_ranking_players_list) == len(lower_ranking_players_list):
            #   verifier durant la boucle dans self.data.rounds_couples si une association de joueurs est deja présente dans les rounds précédents (dans self.data.rounds_couples)
            round_couples = [(upper_ranking_players_list[i], lower_ranking_players_list[i])
                             for i in range(0, len(upper_ranking_players_list))]
            return round_couples
        else:
            return 'These lists do not have the same number of items'

    def enter_new_round(self, round_couples: Union[list[Player], list[tuple], str]):
        if isinstance(round_couples, str):
            return None
        else:
            round_dict = NewRoundForm(self.data).add_new()
            _round = Round(**round_dict)
            for _tuple in round_couples:
                player1_id = _tuple[0].identifier_pod
                player2_id = _tuple[1].identifier_pod
                match_dict = NewMatchForm(self.data, player1_id, player2_id).add_new()
                match = Match(**match_dict)
                _round.matches.append(match)
            self.data.rounds_list.append(_round)
            data.save()  #  "TypeError: Object of type Player is not JSON serializable" (dans Tournament)
            return _round

    def get_round_results(self, _round: Round) -> Round:
        """
        This method gets the match results of a round and adds those players by player to the round
        """
        _round.results = {}
        for match in _round.matches:
            _round.results[match.player1_id_pod] = match.player1_score_pod
            _round.results[match.player2_id_pod] = match.player2_score_pod
        return _round  # ->  Round  avec .result => dict(id:score)

    def add_players_points_to_tournament_totals(self, _round: Round) -> dict:
        """
        This method enables to count the players points after a round
        and add the scores to the tournament results
        """
        if self.data.total_results == {}:
            new_totals = _round.results
        else:
            counter = collections.Counter()
            total_pts_by_player = self.data.total_results, _round.results
            for player_id in total_pts_by_player:
                counter.update(player_id)
            new_totals = dict(counter)
        self.data.total_results = new_totals
        return new_totals
