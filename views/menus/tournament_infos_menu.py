# coding=utf-8
from controllers import list_tournaments_controller, tournament_infos_controller
from views.menus.menu import Menu


class TournamentInfosMenu(Menu):
    """
    This class is the Menu listing all Tournaments management.
    It enables to resume a tournament
    or select one and list infos about the selected tournament
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         root_page=False, previous_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         current_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.resume,
                                 self.sort_players_by_last_name, self.sort_players_by_result,
                                 self.list_rounds, self.list_matches, self.add_round, self.add_match]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def list_all(self):
        """
        This method calls the controller to display all registered tournament instances by start date
        """
        print('List of all Tournaments: ')
        tournaments_list = list_tournaments_controller.ListTournamentsCtrl().list_all_tournaments()
        if len(tournaments_list) == 0:
            print('No tournament in the registry')
        else:
            for tournament in tournaments_list:
                print(f'{tournament.name}, {tournament.location}\n '
                      f'{tournament.start_date}, {tournament.end_date}')
        list_tournaments_controller.ListTournamentsCtrl().run()

    def resume(self):  # list all tournaments and select one tournament # à virer !?
        pass

    def sort_players_by_last_name(self):  # for one selected tournament
        pass

    def sort_players_by_result(self):  # for one selected tournament
        pass

    def list_rounds(self):  # for one selected tournament
        pass

    def list_matches(self):  # for one selected tournament
        pass

    def add_round(self):
        pass

    def add_match(self):
        pass
