# coding=utf-8

from controllers.factory import Factory
from models.player import Player
from views.forms.add_new_player_form import NewPlayerForm
from views.menus.list_players_menu import ListPlayerMenu
from views.menus.menu import Menu
import views.menus.home_menu as home_menu  # import du module plutot que la classe pour eviter le pb d'import circulaire


"""
View file for the Player Database Management Menu.
"""


class PlayerMenu(Menu):
    """
    This class manages a menu to navigate through the Player Database Management.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Players Menu-',
                         previous_page=home_menu.HomeMenu())
        self.previous_page = home_menu.HomeMenu()
        specific_menu_choices = [self.list_all, self.add_new_player, self.edit_player]
        [self.choices.append(choice) for choice in specific_menu_choices]


    def list_all(self): # Mutualiser avec list_all de tournaments dans menu si possible
        ListPlayerMenu().run()

    def add_new_player(self):
        NewPlayerForm().add_new_player()

    def edit_player(self):
        pass

    # defs à revoir



if __name__ == '__main__':
    PlayerMenu().run()
