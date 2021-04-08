# coding=utf-8
from controllers import list_tournaments_controller, tournament_infos_controller
from views.menus.menu import Menu


class TournamentInfosMenu(Menu):
    """
    This class is the Menu for the management of one selected Tournament.
    It enables to display informations about this tournament or update it.
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

    def resume(self):  # list all tournaments and select one tournament # à virer !?
        pass

    def sort_players_by_last_name(self) -> None:  # for one selected tournament
        pass

    def sort_players_by_result(self) -> None:  # for one selected tournament
        pass

    def list_rounds(self) -> None:  # for one selected tournament
        pass

    def list_matches(self) -> None:  # for one selected tournament
        pass

    def add_round(self) -> None:
        pass

    def add_match(self) -> None:
        pass
