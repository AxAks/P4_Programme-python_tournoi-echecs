# coding=utf-8
from controllers.tournament_infos_controller import TournamentInfosCtrl
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
