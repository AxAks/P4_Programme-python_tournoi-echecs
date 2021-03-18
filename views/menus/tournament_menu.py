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
        self.choices = {
            '1': self.new_tournament,
            '2': self.display_all,
            '3': self.edit_player,
            '4': self.save_tournament,
            '5': self.load_tournament,
            '0': self.quit
        }

    def player_menu(self):
        """
        This method displays the different options of the menu: Player Database.
        """
        print('Chess Tournament Manager\n'
              '-Players Menu-\n'
              '\n1. Add New Player\n'
              '2. Search Players\n'
              '3. Edit Players\n'
              '4. Load State\n'
              '5. Save State\n'
              '\n0. Quit')
