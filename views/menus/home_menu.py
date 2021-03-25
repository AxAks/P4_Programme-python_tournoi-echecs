# coding=utf-8

from views.menus.menu import Menu
from controllers import menu_controller


class HomeMenu(Menu):
    """
    This class is the root Menu of the program.
    This is the first screen the user lands on.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Home Menu',
                         root_page=True, exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.manage_players, self.manage_tournaments, self.start_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def manage_players(self) -> None:
        """
        This method leads to the Players Database Manager menu
        """
        menu_controller.to_player_menu()

    def manage_tournaments(self) -> None:
        """
        This method leads to the Tournaments Manager menu
        """
        menu_controller.to_tournament_menu()

    def start_tournament(self) -> None:
        """
        This method enables to start a tournament directly
        """
        pass # la ou on va doublon avec add_new_tournament ?