# coding=utf-8


from views.menus.menu import Menu
import views.menus.home_menu as home_menu
from controllers import menu_controller


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
        menu_controller.to_list_all_tournaments()

    def add_new_tournament(self):
        menu_controller.to_new_tournament_form()

    # defs à ecrire
    def save_tournament(self):
        pass

    def load_tournament(self):
        pass
