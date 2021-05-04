# coding=utf-8

from controllers import list_tournaments_controller, home_controller
from controllers.tournament_infos_controller import TournamentInfosCtrl
from views.menus.menu import Menu


class ListTournamentsMenu(Menu):
    """
    This class is the Menu listing all Tournaments.
    It also enables to select one of them in order to list or update its information.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         root_page=False, previous_page_ctrl=home_controller.HomeCtrl,
                         current_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add_tournament, self.display_by_start_date,
                                 self.display_by_name, self.display_by_location,
                                 self.search_tournaments, self.select_one]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_tournament(self) -> None:
        """
        This method calls the controller to create a new Tournament instance.
        """
        tournament = self.current_page_ctrl().add_tournament()
        self.print_new_tournament_registered()
        self.print_tournament_general_infos(tournament)
        self.current_page_ctrl().run()

    def display_by_start_date(self) -> None:
        """
        This method calls the controller to display all registered tournament instances by start date
        """
        self.header_tournament_by_start_date()
        tournaments_list = self.current_page_ctrl().sort_by_start_date()
        if len(tournaments_list) == 0:
            self.print_no_tournament_found()
        else:
            for tournament in tournaments_list:
                self.print_tournament_infos_simple(tournament)
        self.current_page_ctrl().run()

    def display_by_name(self) -> None:
        self.header_tournament_by_name()
        tournaments_list = self.current_page_ctrl().sort_by_name()
        if len(tournaments_list) == 0:
            self.print_no_tournament_found()
        else:
            for tournament in tournaments_list:
                self.print_tournament_infos_simple(tournament)
        self.current_page_ctrl().run()

    def display_by_location(self) -> None:
        self.header_tournament_by_location()
        tournaments_list = self.current_page_ctrl().sort_by_location()
        if len(tournaments_list) == 0:
            self.print_no_tournament_found()
        else:
            for tournament in tournaments_list:
                self.print_tournament_infos_simple(tournament)
        self.current_page_ctrl().run()

    def search_tournaments(self) -> None:
        """
        This method calls the controller to find one or more Tournament instances in the registry
        """
        self.print_hard_separator()
        self.header_tournaments_search()
        search = self.input_search_a_tournament_by_name_location_dates()
        tournaments = self.current_page_ctrl().search_by_id(search)
        self.header_tournaments_search_results()
        if len(tournaments) == 0:
            self.print_no_tournament_found()
        for tournament in tournaments:
            self.print_tournament_infos_simple(tournament)
        self.current_page_ctrl().run()

    def select_one(self) -> None:
        """
        This method enables to pick a tournament
        and be redirected this the Menu for this specific tournament.
        """

        selected_tournament = self.current_page_ctrl().select_one()
        if selected_tournament == {}:
            self.print_no_tournament_found()
            self.print_please_retry()
            self.current_page_ctrl().run()
        else:
            self.print_one_tournament_found()
            self.print_tournament_general_infos(selected_tournament)
            TournamentInfosCtrl(selected_tournament).run()
