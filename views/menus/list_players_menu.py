# coding=utf-8
from controllers import player_controller
from models.player import Player
from views.menus.menu import Menu
import views.menus.player_menu as player_menu  # import du module plutot que la classe pour eviter le pb d'import circulaire


class ListPlayerMenu(Menu):
    """
    This class is a menu used to display sorted or filtered lists of Players from the Database.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Players Reports Menu',
                         previous_page=player_menu.PlayerMenu())
        specific_menu_choices = [self.sort_by_last_name, self.sort_by_ranking,
                                 self.search_by_id, self.search_by_last_name]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_by_last_name(self):
        """
        This method directs to the player controller
        to get a list of all players sorted by last name
        and displays this list
        """
        print('All Players by Last Name')
        sorted_by_last_name = player_controller.sort_by_last_name()
        for player_obj in sorted_by_last_name:
            print(f'{player_obj.identifier}, '
                  f'{player_obj.last_name}, {player_obj.first_name}: '
                  f' {player_obj.birthdate}, '
                  f' {player_obj.ranking}, '
                  f'{player_obj.gender_pod}')

    def sort_by_ranking(self):
        """
        This method directs to the player controller
        to get a list of all players sorted by ranking
        and displays this list
        """
        print('All Players by Ranking:')
        sorted_by_ranking = player_controller.sort_by_ranking()
        for player_obj in sorted_by_ranking:
            print(f'{player_obj.identifier}, '
                  f'{player_obj.last_name}, {player_obj.first_name}: '
                  f' {player_obj.birthdate}, '
                  f' {player_obj.ranking}, '
                  f'{player_obj.gender_pod}')

    def search_by_id(self):
        pass

    def search_by_last_name(self):
        pass

