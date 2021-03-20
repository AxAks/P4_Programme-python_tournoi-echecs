# coding=utf-8

from controllers.factory import Factory
from models.player import Player
from views.menus.menu import Menu
import views.menus.player_menu as player_menu  # import du module plutot que la classe pour eviter le pb d'import circulaire


"""
View file for the Player Reports Management Menu.
"""


class ListPlayerMenu(Menu):
    """
    This class manages a menu to navigate through the Player Database Management.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Players Reports Menu-')
        specific_menu_choices = [self.sort_by_last_name, self.sort_by_ranking, self.search_player]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def back(self) -> None:
        """
        This method enables to go back to the previous screen
        It leads to the Home Menu which is the previous menu screen at this level.
        """
        print('Back to previous Menu Screen')
        player_menu.PlayerMenu().run()

    def sort_by_last_name(self):
        pass

    def sort_by_ranking(self):
        pass

    def search_player(self):
        pass