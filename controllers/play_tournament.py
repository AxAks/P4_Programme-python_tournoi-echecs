# coding=utf-8
from controllers.tournament_infos_controller import TournamentInfosCtrl
from controllers.list_tournaments_controller import ListTournamentsCtrl
from controllers.tournaments_controller import TournamentCtrl


class PlayTournament:
    """
    This class defines the proceeding of a tournament
    """
    def __init__(self, tournament=None):
        self.tournament = tournament

    def add_new_tournament(self):
        tournament = TournamentCtrl().add_tournament()
        TournamentInfosCtrl(tournament).run()

    def select_tournament(self):
        tournament = ListTournamentsCtrl().select_one()
        TournamentInfosCtrl(tournament).run()
