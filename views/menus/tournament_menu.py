# coding=utf-8

from views.menus.menu import Menu
import views.menus.home_menu as home_menu
"""
View file for the Tournament Management Menu.
"""


class TournamentMenu(Menu):
    """
    This class manages a menu to navigate through the Tournament Management.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Tournaments Menu-')
        specific_menu_choices = [self.list_all_tournaments, self.create_new_tournament,
                                 self.save_tournament, self.load_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]


    #  on recupère def run() et def back() (avec un if) via l'héritage de Menu car il sont toujours identiques

    def back(self) -> None:
        """
        This method enables to go back to the previous screen
        It leads to the Home Menu which is the previous menu screen at this level.
        """
        print('Back to previous Menu Screen')
        home_menu.HomeMenu().run()

    # defs à ecrire !
    def create_new_tournament(self):
        pass

    def list_all_tournaments(self):
        pass

    def save_tournament(self):
        pass

    def load_tournament(self):
        pass


if __name__ == '__main__':
    TournamentMenu().run()
