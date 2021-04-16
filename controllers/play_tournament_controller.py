# coding=utf-8
from controllers.tournament_infos_controller import TournamentInfosCtrl
from controllers.list_tournaments_controller import ListTournamentsCtrl
from controllers.tournaments_controller import TournamentCtrl
from views.forms.new_match_form import NewMatchForm
from views.forms.new_round_form import NewRoundForm


class PlayTournamentCtrl:  # à faire !
    """
    This class defines the proceeding of a tournament
    """
    def __init__(self, tournament=None):
        self.tournament = tournament

    def add_new_tournament(self):
        new_tournament = TournamentCtrl().add_tournament()
        tournament_controller = TournamentInfosCtrl(new_tournament)
        tournament = tournament_controller.data
        while len(tournament.rounds_list) != tournament.rounds:
            self.generate_matchups()
            NewRoundForm.add_new()
            NewMatchForm.add_new()
            self.add_players_scores()

        tournament_controller.run()

    def select_tournament(self):
        new_tournament = ListTournamentsCtrl().select_one()
        tournament_controller = TournamentInfosCtrl(new_tournament)
        tournament = tournament_controller.data
        while len(tournament.rounds_list) != tournament.rounds:
            self.generate_matchups()
            NewRoundForm.add_new()
            NewMatchForm.add_new()
            self.add_players_scores()

        tournament_controller.run()

    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass

    def add_players_scores(self):
        """
        This method enables to count the players points after a round
        and caculate the scores and ranking inside the tournament
        """
        pass