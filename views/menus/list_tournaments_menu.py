# coding=utf-8
from controllers import tournament_controller
from views.menus.menu import Menu
from views.menus import tournament_menu   # import du module plutot que la classe pour eviter le pb d'import circulaire


class ListTournamentsMenu(Menu):
    """
    This class is a menu used to display sorted or filtered lists related to Tournaments.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Reports Menu',
                         previous_page=tournament_menu.TournamentMenu())
        specific_menu_choices = [self.sort_by_name, self.sort_by_location,
                                 self.sort_by_start_date, self.search_by_id, self.display_tournament_players,
                                 self.display_tournament_rounds, self.display_tournament_matches]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_name(self):  # à reprendre à cause des listes : players, rounds (et match ?)
        """
        This method directs to the tournament controller
        to get a list of all tournaments sorted by name
        and displays this list
        """
        print('All Tournaments by Name')
        sorted_by_name = tournament_controller.sort_by_name()
        for tournament_obj in sorted_by_name:
            print(f'{tournament_obj.name}, '
                  f'{tournament_obj.location}, {tournament_obj.start_date} {tournament_obj.end_date}: \n'
                  f' {tournament_obj.identifiers_list}, '
                  f' {tournament_obj.time_control_pod}, '
                  f'{tournament_obj.description}, '
                  f'{tournament_obj.rounds_list}, ' 
                  f'{tournament_obj.rounds}')

    def sort_by_location(self):
        """
        This method directs to the tournament controller
        to get a list of all tournaments sorted by location
        and displays this list
        """
        print('All Tournaments by Location')
        sorted_by_location = tournament_controller.sort_by_location()
        for tournament_obj in sorted_by_location:
            print(f'{tournament_obj.name}, '
                  f'{tournament_obj.location}, {tournament_obj.start_date} {tournament_obj.end_date}: \n'
                  f' {tournament_obj.identifiers_list}, '
                  f' {tournament_obj.time_control_pod}, '
                  f'{tournament_obj.description}, '
                  f'{tournament_obj.rounds_list}, '
                  f'{tournament_obj.rounds}')

    def sort_by_start_date(self):
        """
        This method directs to the tournament controller
        to get a list of all tournaments sorted by start date
        and displays this list
        """
        print('All Tournaments by Start Date')
        sorted_by_start_date = tournament_controller.sort_by_start_date()
        for tournament_obj in sorted_by_start_date:
            print(f'{tournament_obj.name}, '
                  f'{tournament_obj.location}, {tournament_obj.start_date} {tournament_obj.end_date}: \n'
                  f' {tournament_obj.identifiers_list}, '
                  f' {tournament_obj.time_control_pod}, '
                  f'{tournament_obj.description}, '
                  f'{tournament_obj.rounds_list}, '
                  f'{tournament_obj.rounds}')

    def search_by_id(self):
        """
        This method directs to the tournament controller
        to get a list of tournaments matching the given information.
        It then displays this list.
        """
        _input = input('Search a tournament by Name, Location or dates: ')
        results = tournament_controller.search_by_id(_input)
        print('Tournaments found:')
        for tournament_obj in results:
            print(f'{tournament_obj.name}, '
                  f'{tournament_obj.location}, {tournament_obj.start_date} {tournament_obj.end_date}: \n'
                  f' {tournament_obj.identifiers_list}, '
                  f' {tournament_obj.time_control_pod}, '
                  f'{tournament_obj.description}, '
                  f'{tournament_obj.rounds_list}, '
                  f'{tournament_obj.rounds}')


    def display_tournament_players(self):
        """
        This method directs to the tournament controller
        to get the list of players for a given tournament.
        It then displays this list.
        """
        # à faire
        tournament_controller.display_tournament_players()

    def display_tournament_rounds(self):
        """
        This method directs to the tournament controller
        to get the list of rounds for a given tournament.
        It then displays this list.
        """
        #  à faire
        tournament_controller.display_tournament_rounds()

    def display_tournament_matches(self):
        """
        This method directs to the tournament controller
        to get the list of matches for a given tournament.
        It then displays this list.
        """
        #  à faire
        tournament_controller.display_tournament_matches()