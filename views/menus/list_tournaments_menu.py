# coding=utf-8
from controllers import tournaments_controller, list_tournaments_controller
from views.menus.menu import Menu


class ListTournamentsMenu(Menu):
    """
    This class is the Menu listing all Tournaments.
    It also enables to select one of them in order to list or update its information.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         root_page=False, previous_page_ctrl=tournaments_controller.TournamentCtrl,
                         current_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.sort_by_start_date, self.sort_by_name, self.sort_by_location,
                                 self.search_by_id, self.select_one]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_start_date(self):  # list all tournaments
        """
        This method calls the controller to display all registered tournament instances by start date
        """
        print('========================')
        print('List of all Tournaments sorted by Start Date: ')
        print('========================')
        tournaments_list = self.current_page_ctrl().sort_by_start_date()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'{tournament.start_date}, {tournament.end_date}\n'
                      f'-> {tournament.name}, {tournament.location}')
        self.current_page_ctrl().run()

    def sort_by_name(self):
        print('========================')
        print('List of all Tournaments sorted by Start Date: ')
        print('========================')
        tournaments_list = self.current_page_ctrl().sort_by_name()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'{tournament.name}, {tournament.location}\n '
                      f'-> {tournament.start_date}, {tournament.end_date}')
        self.current_page_ctrl().run()

    def sort_by_location(self):
        print('========================')
        print('List of all Tournaments sorted by Location: ')
        print('========================')
        tournaments_list = self.current_page_ctrl().sort_by_location()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'{tournament.location}, {tournament.name}\n '
                      f'->{tournament.start_date}, {tournament.end_date}')
        self.current_page_ctrl().run()

    def search_by_id(self):  # à détailler, affiche actuellement l'objet, print les attributs! et verifier le focntionnement !
        search = input('Search a Tournament by Name, Location or dates : ')
        print(self.current_page_ctrl().search_by_id(search))
        self.current_page_ctrl().run()

    def select_one(self):  #  prints and select one tournament
        print(self.current_page_ctrl().select_one())
        self.current_page_ctrl().select_one()  # pas encore fait en fait, à faire !
        self.current_page_ctrl().run()  # à voir
