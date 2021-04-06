# coding=utf-8
from controllers import tournament_controller, list_tournaments_controller
from views.menus.menu import Menu


class ListTournamentMenu(Menu):
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
        specific_menu_choices = [self.list_all_tournaments, self.select, self.resume,
                                 self.sort_players_by_last_name, self.sort_players_by_result,
                                 self.list_rounds, self.list_matches]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all_tournaments(self):
        """
        This method calls the controller to display all registered tournament instances by start date
        """
        print('List of all Tournaments: ')
        for tournament in list_tournaments_controller.ListTournamentsCtrl().list_all_tournaments():
            print(f'{tournament.name}, {tournament.location}\n '
                  f'{tournament.start_date}, {tournament.end_date}')
        list_tournaments_controller.ListTournamentsCtrl().run()

    def select(self):  # list all tournaments and select one tournament
        pass

    def resume(self):  # resume selected tournament
        pass

    def sort_players_by_last_name(self):  # for one selected tournament
        pass

    def sort_players_by_result(self):  # for one selected tournament
        pass

    def list_rounds(self):  # for one selected tournament
        pass

    def list_matches(self):  # for one selected tournament
        pass
