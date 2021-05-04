# coding=utf-8
from controllers import home_controller
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
        specific_menu_choices = [self.launch_new_tournament, self.search_registered_tournament_to_resume,
                                 self.manage_players, self.manage_tournaments]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def launch_new_tournament(self):
        """
        This method calls the controller to create a new tournament
        and start it directly
        """
        self.current_page_ctrl().launch_new_tournament()

    def search_registered_tournament_to_resume(self):
        """
        this method calls the controller to search a previously saved tournament
        """
        print('========================')
        print('Tournament Selection: ')
        print('========================')
        self.current_page_ctrl().search_registered_tournament()

    def manage_players(self) -> None:
        """
        This method calls the controller to redirect to the Players Menu
        """
        self.current_page_ctrl().manage_players()

    def manage_tournaments(self) -> None:
        """
        This method calls the controller to redirect to the Tournaments Menu
        """
        self.current_page_ctrl().manage_tournaments()
