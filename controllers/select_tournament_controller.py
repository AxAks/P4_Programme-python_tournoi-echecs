# coding=utf-8

from controllers.controller import Controller
from views.menus.select_tournament_menu import SelectTournamentMenu


class SelectTournamentCtrl(Controller):
    def __init__(self):
        self.menu = SelectTournamentMenu()

    def select(self):
        pass