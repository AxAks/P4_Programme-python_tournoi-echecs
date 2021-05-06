# coding=utf-8

from controllers.controller import Controller
from controllers import players_controller, list_tournaments_controller
from controllers import tournament_infos_controller
from views.menus.home_menu import HomeMenu


class HomeCtrl(Controller):
    """
    Controller Class for the Home Menu
    It specifies the corresponding Menu page
    """

    def __init__(self):
        self.menu = HomeMenu()
        self.data = None

    def launch_new_tournament(self) -> None:
        """
        This method enables to create and launch a new tournament
        """
        self.data = list_tournaments_controller.ListTournamentsCtrl().add_tournament()
        tournament_infos_controller.TournamentInfosCtrl(self.data).run()

    def search_registered_tournament(self) -> None:
        """
        This method enables to search an existing tournament and go to its menu
        """
        self.data = list_tournaments_controller.ListTournamentsCtrl().select_one()
        self.menu.print_one_tournament_found()
        self.menu.print_tournament_with_descr(self.data)
        tournament_infos_controller.TournamentInfosCtrl(self.data).run()

    def manage_players(self) -> None:
        """
        This method directs to the Players Menu via the player controller
        """
        players_controller.PlayersCtrl().run()

    def manage_tournaments(self) -> None:
        """
        This method directs to the Tournaments Menu via the Tournament controller
        """
        list_tournaments_controller.ListTournamentsCtrl().run()
