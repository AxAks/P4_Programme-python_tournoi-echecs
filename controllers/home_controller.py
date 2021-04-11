# coding=utf-8

from controllers.controller import Controller
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
        This method enables to launch a new tournament
        """
        pass

    def resume_tournament(self):  # à faire !
        """
        This method enables to resume a tournament
        """
        pass
