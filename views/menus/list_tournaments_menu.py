# coding=utf-8
from controllers import tournament_controller, list_tournaments_controller
from views.menus.menu import Menu


class ListTournamentsMenu(Menu):
    """
    This class is the Menu listing all Tournaments management.
    It enables to resume a tournament
    or select one and list infos about the selected tournament
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         root_page=False, previous_page_ctrl=tournament_controller.TournamentCtrl,
                         current_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.list_all, self.select]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all(self): # list all tournaments
        """
        This method calls the controller to display all registered tournament instances by start date
        """
        print('List of all Tournaments: ')
        tournaments_list = self.current_page_ctrl().list_all_tournaments()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'{tournament.name}, {tournament.location}\n '
                      f'{tournament.start_date}, {tournament.end_date}')
        self.current_page_ctrl().run()

    def select_one(self):  #  prints and select one tournament
        print(self.current_page_ctrl().select())
        return self.current_page_ctrl().select()
