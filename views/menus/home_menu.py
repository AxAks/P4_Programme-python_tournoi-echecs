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
        specific_menu_choices = [self.start_tournament, self.resume_tournament,
                                 self.manage_players, self.manage_tournaments]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def start_tournament(self):  # à faire !
        """

        """
        """
        Create new tournament
        envoyer sur la page de ce tournament
        
        """
        self.current_page_ctrl().start_tournament()

    def resume_tournament(self):  # à faire !
        """

        """
        """
        choisir le tournament
        aller sur la page du tournoi
        
        """

        self.current_page_ctrl().resume_tournament()

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
