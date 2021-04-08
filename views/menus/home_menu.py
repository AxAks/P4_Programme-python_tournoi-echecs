# coding=utf-8
from controllers import home_controller
from controllers.players_controller import PlayerCtrl
from controllers.tournaments_controller import TournamentCtrl
from views.menus.menu import Menu


class HomeMenu(Menu):
    """
    This class is the root Menu of the program.
    This is the first screen the user lands on.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Home Menu',
                         root_page=True, current_page_ctrl=home_controller.HomeCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.manage_players, self.manage_tournaments]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def manage_players(self) -> None:
        """
        This method directs to the Players Menu via the player controller
        """
        PlayerCtrl().run()

    def manage_tournaments(self) -> None:
        """
        This method directs to the Tournaments Menu via the Tournament controller
        """
        TournamentCtrl().run()
