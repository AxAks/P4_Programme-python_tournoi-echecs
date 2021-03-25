# coding=utf-8

from views.menus.list_players_menu import ListPlayerMenu
from views.menus.menu import Menu
import views.menus.home_menu as home_menu
from controllers import menu_controller


class PlayerMenu(Menu):
    """
    This class manages a menu to navigate through the Player Database Management.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Players Menu',
                         previous_page=home_menu.HomeMenu())
        self.previous_page = home_menu.HomeMenu()
        specific_menu_choices = [self.list_all, self.add_new_player, self.edit_player]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all(self):
        menu_controller.to_list_all_players()

    def add_new_player(self):
        menu_controller.to_new_player_form()

    def edit_player(self):
        pass
