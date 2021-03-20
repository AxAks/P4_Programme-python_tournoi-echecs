# coding=utf-8

from views.menus.menu import Menu
from views.menus import tournament_menu   # import du module plutot que la classe pour eviter le pb d'import circulaire

"""
View file for the Tournaments Reports Management Menu.
"""


class ListTournamentsMenu(Menu):
    """
    This class is a menu used to display sorted or filtered lists related to Tournaments.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Tournaments Reports Menu-',
                         previous_page=tournament_menu.TournamentMenu())
        specific_menu_choices = [self.sort_by_name, self.sort_by_location, self.search_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_name(self):  # on peut gérer tous les attributs de Tournaments
        pass

    def sort_by_location(self):
        pass

    def search_tournament(self):
        pass
