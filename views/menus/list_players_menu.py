# coding=utf-8

from views.menus.menu import Menu
import views.menus.player_menu as player_menu  # import du module plutot que la classe pour eviter le pb d'import circulaire


"""
View file for the Player Reports Management Menu.
"""


class ListPlayerMenu(Menu):
    """
    This class is a menu used to display sorted or filtered lists of Players from the Database.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Players Reports Menu-',
                         previous_page=player_menu.PlayerMenu())
        specific_menu_choices = [self.sort_by_last_name, self.sort_by_ranking, self.search_player]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_last_name(self):  # on peut gérer tous les attributs de Player
        pass

    def sort_by_ranking(self):
        pass

    def search_player(self):
        pass
