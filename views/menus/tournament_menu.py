# coding=utf-8

import sys

from controllers.factory import Factory
from models.tournament import Tournament
from views.menus.menu import Menu

"""
View file for the Tournament Management Menu.
"""


class TournamentMenu(Menu):
    """
    This class manages a menu to navigate through the Tournament Management.
    """

    def __init__(self):
        super().__init__()  # initialise les choix généraux depuis Menu
        specific_menu_choices = [self.list_all_tournaments, self.create_new_tournament,
                                 self.save_tournament, self.load_tournament]  # liste des choix spécifiques de TournamentMenu
        [self.choices.append(choice) for choice in specific_menu_choices]  # ajoute les spécificités de TournamentMenu à la liste de choix


    #  on recupère run() via l'héritage de Menu

    def tournaments_menu(self):
        """
        This method displays the different options of the menu: Tournaments Management.
        """
        print('Chess Tournament Manager\n'
              '-Tournaments Menu-\n')


    #defs à ecrire !

    def create_new_tournament(self):
        pass

    def list_all_tournaments(self):
        pass

    def save_tournament(self):
        pass

    def load_tournament(self):
        pass


if __name__ == '__main__':
    TournamentMenu().run()