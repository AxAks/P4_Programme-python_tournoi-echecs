# coding=utf-8
from controllers import player_controller
from views.menus.menu import Menu


class PlayerMenu(Menu):
    """
    This class is the Menu for Player management.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Home Menu',
                         root_page=True, exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add, self.search_by_id, self.sort_by_last_name, self.sort_by_ranking]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add(self):
        player_controller.add_player()
        player_controller.run()

    def search_by_id(self):
        _input = input('search a player by ID: ')
        print('Players found: ')
        for player in player_controller.search_by_id(_input):
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.run()

    def sort_by_last_name(self):
        print('All Players by last name: ')
        for player in player_controller.sort_by_last_name():
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.run()

    def sort_by_ranking(self):
        print('All Players by ranking: ')
        for player in player_controller.sort_by_ranking():
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.run()
