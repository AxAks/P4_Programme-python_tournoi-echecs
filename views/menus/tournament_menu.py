# coding=utf-8
from views.menus.menu import Menu


class TournamentMenu(Menu):
    """
    This class is the Menu for Tournaments management.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Home Menu',
                         root_page=True, exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add, self.resume, self.add_round, self.add_match,
                                 self.list, self.select, self.list_players_by_last_name, self.list_players_by_result,
                                 self.list_rounds, self.list_matches]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add(self):
        pass

    def resume(self):
        pass

    def add_round(self):
        pass

    def add_match(self):
        pass

    def list(self):
        pass

    def select(self):
        pass

    def list_players_by_last_name(self):
        pass

    def list_players_by_result(self):
        pass

    def list_rounds(self):
        pass

    def list_matches(self):
        pass