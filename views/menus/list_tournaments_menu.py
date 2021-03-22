# coding=utf-8

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
                                 self.sort_by_start_date, self.search_by_id]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_name(self):
        pass

    def sort_by_location(self):
        pass

    def sort_by_start_date(self):
        pass

    def search_by_id(self):
        pass
