# coding=utf-8

from views.forms.new_tournament_form import NewTournamentForm
from views.menus.menu import Menu
from views.menus.list_tournaments_menu import ListTournamentsMenu

import views.menus.home_menu as home_menu


class TournamentMenu(Menu):
    """
    This class manages a menu to navigate through the Tournament Management.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         previous_page=home_menu.HomeMenu())
        specific_menu_choices = [self.list_all, self.add_new_tournament,
                                 self.save_tournament, self.load_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all(self):
        ListTournamentsMenu().run()

    # defs à ecrire !
    def add_new_tournament(self):
        NewTournamentForm().add_new_tournament()


    def save_tournament(self):
        pass

    def load_tournament(self):
        pass
