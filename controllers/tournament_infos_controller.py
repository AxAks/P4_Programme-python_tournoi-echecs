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
from utils import clear_terminal
from views.forms.new_match_form import NewMatchForm
from views.forms.new_player_form import NewPlayerForm
from views.forms.new_round_form import NewRoundForm
from views.menus.tournament_infos_menu import TournamentInfosMenu


class TournamentInfosCtrl(Controller):
    """
    Controller class for a specific Tournament Menu Page once the tournament is selected.
    """

    def __init__(self, tournament=None):
        self.menu = TournamentInfosMenu(tournament)
        self.data = tournament

    def proceed_tournament(self) -> None:
        """
        This method enables to resume the current tournament
        """
        if self.tournament_algorithm() is None:
            return None
        else:
            TournamentInfosCtrl(self.data).run()

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

    @staticmethod
    def sort_players_by_result(tournament: Tournament) -> Union[list[Player], Any]:
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

    def display_not_played_yet(self) -> dict[Player]:
        """
        This method lists for each player the opponents they have not played against
         in the previous rounds of a given tournament
        """
        return self.data.not_played_yet

    def get_nb_rounds_played(self) -> int:
        """
        This method returns the number of rounds
        already played for a given tournament
        """
        return len(self.data.rounds_list)

    def get_total_nb_rounds(self) -> int:
        """
        this method returns the total number of rounds for a given tournament
        """
        return self.data.rounds

    def display_rounds_and_matches(self) -> list:
        """
        This method lists all the rounds of a given tournament
        """
        return self.data.rounds_list

    def tournament_algorithm(self) -> None:
        """
        This method is the main algorithm for the progression of a tournament.
        It checks at which step the tournament is
        and enables to proceed next steps
        """
        if len(self.data.rounds_list) >= self.data.rounds and not self.data.done:
            tmp_list = []
            [tmp_list.append(self.data.not_played_yet[player])
             for player in self.data.not_played_yet if
             len(self.data.not_played_yet[player]) != 0]

            if len(tmp_list) == 0:
                self.menu.print_all_players_have_played()
            self.menu.print_update_rankings()
            self.update_tournaments_players_rankings()
            self.data.done = True
            data.save()
            return None

        else:
            while len(self.data.rounds_list) < self.data.rounds:
                matchups_next_round = self.get_next_round_matchups()
                next_round = self.enter_new_round(matchups_next_round)
                self.get_round_results(next_round)
                self.add_players_points_to_tournament_totals(next_round)
                data.save()
                TournamentInfosCtrl(self.data).run()

    def get_next_round_matchups(self) -> Union[list[Player], list[list], str]:
        """
        This method generates the tournament match-ups between the Players for a new round.
        It takes into account the players general rankings and/or results in the tournament
        and whether it is the first round or another round
        """
        if len(self.data.rounds_list) == 0:
            sorted_players_obj = self.sort_tournament_players_by_ranking()
        else:
            sorted_players_results = self.sort_players_by_result(self.data)
            sorted_players_obj = [_tuple[0] for _tuple in sorted_players_results]
        round_couples = self.get_round_couples(sorted_players_obj)
        return round_couples

    def get_round_couples(self, sorted_players: Union[list, dict]) -> Union[list[list[Player]], str]:
        """
        This method calculates the rounds matchups.
        It checks that the players have not already played together in the previous rounds
        """
        if len(sorted_players) % 2 == 0:
            middle_index = len(sorted_players) // 2
            upper_ranking_players_list = sorted_players[:middle_index]
            lower_ranking_players_list = sorted_players[middle_index:]
        else:
            return 'This list does not have an even number of items'

        if len(self.data.rounds_list) == 0:
            round_couples = [[upper_ranking_players_list[i], lower_ranking_players_list[i]]
                             for i in range(0, len(upper_ranking_players_list))]
            return round_couples
        else:
            round_couples = []
            while len(sorted_players) > 0:
                player1 = sorted_players[0]
                player1_id = player1.identifier_pod
                sorted_players.pop(0)
                for player2 in sorted_players:
                    if player2.identifier_pod in self.data.not_played_yet[player1_id]:
                        round_couples.append([player1, player2])
                        sorted_players.remove(player2)
                        break
            return round_couples

    def enter_new_round(self, round_couples: Union[list[list[Player]], str]) -> Union[Round, None]:
        """
        This method enables to register a new round with the matches results.
        It also removes the matchups from the potential matchups for next rounds
        in order to avoid two players to play together twice
        """
        if isinstance(round_couples, str):
            return None
        else:
            round_dict = NewRoundForm(self.data).add_new()
            _round = Round(**round_dict)
            clear_terminal()
            self.menu.print_new_round_registered()
            print(_round)
            for _list in round_couples:
                player1_id = _list[0].identifier_pod
                player2_id = _list[1].identifier_pod
                match_dict = NewMatchForm(self.data, player1_id, player2_id).add_new()
                match = Match(**match_dict)
                clear_terminal()
                self.menu.print_new_match_registered()
                print(match)
                self.menu.print_hard_separator()
                _round.matches.append(match)
                self.data.not_played_yet[player1_id].remove(player2_id)
                self.data.not_played_yet[player2_id].remove(player1_id)
            self.data.rounds_list.append(_round)
            clear_terminal()
            print(_round)
            data.save()
            return _round

    @staticmethod
    def get_round_results(_round: Round) -> Round:
        """
        This method gets the matches results of a round and adds those players by player to the round
        """
        _round.results = {}
        for match in _round.matches:
            _round.results[match.player1_id_pod] = match.player1_score_pod
            _round.results[match.player2_id_pod] = match.player2_score_pod
        return _round

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

    def update_tournaments_players_rankings(self) -> dict:
        self.menu.header_tournament_player_ranking_update()
        new_rankings = {}
        for identifier in self.data.identifiers_list:
            clear_terminal()
            player = PlayerManager().from_identifier_to_player_obj(identifier)
            print(player)
            new_ranking = NewPlayerForm().ask_ranking()
            player.ranking = new_ranking
            print(f'New Ranking: {player.ranking}')
            self.menu.print_hard_separator()
            new_rankings[player] = new_ranking
        return new_rankings

    @staticmethod
    def add_round_start_time() -> datetime:
        """
        This method automatically sets the start time of the Round Object
        """
        return datetime.now()

    @staticmethod
    def add_round_end_time() -> datetime:
        """
        This method automatically sets the end time of the Round Object
        """
        return datetime.now()
