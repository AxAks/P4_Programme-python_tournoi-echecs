# coding=utf-8
from controllers import home_controller, tournament_controller, list_tournaments_controller
from views.menus.menu import Menu


class TournamentsMenu(Menu):
    """
    This class is the Menu for Tournaments management.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         root_page=False, previous_page_ctrl=home_controller.HomeCtrl,
                         current_page_ctrl =tournament_controller.TournamentCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add_tournament, self.to_tournaments_list]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_tournament(self):
        tournament = tournament_controller.TournamentCtrl().add_tournament()
        print(f'New Tournament registered:\n'
              f'{tournament.name}, {tournament.location},\n'
              f'{tournament.start_date}, {tournament.end_date}, {tournament.identifiers_list},'
              f' {tournament.time_control}, {tournament.description}')
        self.current_page_ctrl().run()

    def to_tournaments_list(self):
        """
        This method directs to the Tournament Lists Menu via the Tournament Lists controller
        """
        list_tournaments_controller.ListTournamentsCtrl().run()

