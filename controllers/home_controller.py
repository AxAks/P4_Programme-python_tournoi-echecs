# coding=utf-8

from controllers.controller import Controller
from controllers import players_controller
from controllers import tournaments_controller
from controllers import tournament_infos_controller
from views.menus.home_menu import HomeMenu


class HomeCtrl(Controller):
    """
    Controller Class for the Home Menu
    It specifies the corresponding Menu page
    """

    def __init__(self):
        self.menu = HomeMenu()

    def start_tournament(self):  # à faire !
        """
        This method enables to launch and run a new tournament
        """
        tournament_infos_controller.TournamentInfosCtrl().add_new_tournament()

    def resume_tournament(self, ):  # à faire !
        """
        This method enables to resume an existing tournament
        """
        tournament_infos_controller.TournamentInfosCtrl().select_tournament()

    def manage_tournaments(self) -> None:
        """
        This method directs to the Tournaments Menu via the Tournament controller
        """
        tournaments_controller.TournamentCtrl().run()

    def manage_players(self) -> None:
        """
        This method directs to the Players Menu via the player controller
        """
        players_controller.PlayerCtrl().run()
