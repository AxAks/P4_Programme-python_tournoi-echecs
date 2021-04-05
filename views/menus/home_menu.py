# coding=utf-8
from controllers import player_controller, tournament_controller
from views.menus.menu import Menu


class HomeMenu(Menu):
    """
    This class is the root Menu of the program.
    This is the first screen the user lands on.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Home Menu',
                         root_page=True, exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.manage_players, self.manage_tournaments]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def manage_players(self):
        player_controller.run()

    def manage_tournaments(self):
        tournament_controller.run()
