# coding=utf-8

from controllers import tournaments_controller, list_tournaments_controller
from controllers.tournament_infos_controller import TournamentInfosCtrl
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
        specific_menu_choices = [self.display_by_start_date, self.display_by_name, self.display_by_location,
                                 self.search_by_id, self.select_one]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def display_by_start_date(self) -> None:
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
                print(f'- from {tournament.start_date} to {tournament.end_date}\n'
                      f'-> {tournament.name} in {tournament.location}')
        self.current_page_ctrl().run()

    def display_by_name(self) -> None:
        print('========================')
        print('List of all Tournaments by Start Date: ')
        print('========================')
        tournaments_list = self.current_page_ctrl().sort_by_name()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'- {tournament.name} in {tournament.location}\n '
                      f'-> from {tournament.start_date} to {tournament.end_date}')
        self.current_page_ctrl().run()

    def display_by_location(self) -> None:
        print('========================')
        print('List of all Tournaments by Location: ')
        print('========================')
        tournaments_list = self.current_page_ctrl().sort_by_location()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'- {tournament.location}, {tournament.name}\n '
                      f'-> from {tournament.start_date} to {tournament.end_date}')
        self.current_page_ctrl().run()

    def search_by_id(self) -> None:
        """
        This method calls the controller to find one or more Tournament instances in the registry
        """
        print('========================')
        search = input('Search a Tournament by Name, Location or dates : ')
        tournaments = self.current_page_ctrl().search_by_id(search)
        print('========================')
        print('Tournament Search Results: ')
        print('========================')
        if len(tournaments) == 0:
            print('No Tournament found for this request')
        for tournament in tournaments:
            print(f'- {tournament.location}, {tournament.name}\n'
                  f'-> from {tournament.start_date} to {tournament.end_date}')
        self.current_page_ctrl().run()

    def select_one(self) -> None:
        """
        This method enables to pick a tournament
        and be redirected this the Menu for this specific tournament.
        """
        selected_tournament = self.current_page_ctrl().select_one()
        if selected_tournament == {}:
            print("No Tournament found in Registry for this research")
            self.current_page_ctrl().run()
        else:
            print('1 Tournament found in Registry for this research:')
            print(f'- {selected_tournament.name}, '
                  f'{selected_tournament.location}, '
                  f'{selected_tournament.start_date}, '
                  f'{selected_tournament.end_date}\n'
                  f'-> {selected_tournament.description}')
        TournamentInfosCtrl(selected_tournament).run()
