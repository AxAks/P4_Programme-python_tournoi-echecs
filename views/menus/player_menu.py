# coding=utf-8
from controllers import player_controller, home_controller
from views.menus.menu import Menu


class PlayerMenu(Menu):
    """
    This class is the Menu for Player management.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Players Menu',
                         root_page=False, previous_page_ctrl=home_controller.HomeCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add, self.search_by_id, self.sort_by_last_name, self.sort_by_ranking]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add(self):
        player = player_controller.PlayerCtrl().add_player()
        print(f'New Player registered:\n'
              f'{player.last_name}, {player.first_name},\n'
              f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}, {player.identifier_pod}')
        player_controller.PlayerCtrl().run()

    def search_by_id(self):
        _input = input('search a player by ID: ')
        print('Players found: ')
        for player in player_controller.PlayerCtrl().search_by_id(_input):
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.PlayerCtrl().run()

    def sort_by_last_name(self):
        print('All Players by last name: ')
        for player in player_controller.PlayerCtrl().sort_by_last_name():
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.PlayerCtrl().run()

    def sort_by_ranking(self):
        print('All Players by ranking: ')
        for player in player_controller.PlayerCtrl().sort_by_ranking():
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        player_controller.PlayerCtrl().run()
