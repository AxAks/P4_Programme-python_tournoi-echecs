# coding=utf-8
from controllers import player_controller, home_controller
from views.menus.menu import Menu


class PlayersMenu(Menu):
    """
    This class is the Menu for Player management.
    """
    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Players Menu',
                         root_page=False, previous_page_ctrl=home_controller.HomeCtrl,
                         current_page_ctrl=player_controller.PlayerCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add, self.search_by_id, self.sort_by_last_name, self.sort_by_ranking]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add(self) -> None:
        """
        This method calls the controller to create a player instance
        """
        player = self.current_page_ctrl().add_player()
        print(f'New Player registered:\n'
              f'{player.last_name}, {player.first_name},\n'
              f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}, {player.identifier_pod}')
        self.current_page_ctrl().run()

    def search_by_id(self) -> None:
        """
        This method calls the controller to find one or more player instances in the registry
        """
        print('========================')
        _input = input('search a player by ID: ')
        print('========================')
        print('Players found: ')
        for player in self.current_page_ctrl().search_by_id(_input):
            print(f'{player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        self.current_page_ctrl().run()

    def sort_by_last_name(self) -> None:
        """
        This method calls the controller to sort all player instances by last name
        """
        print('========================')
        print('All Players by last name: ')
        print('========================')
        for player in self.current_page_ctrl().sort_by_last_name():
            print(f'- {player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        self.current_page_ctrl().run()

    def sort_by_ranking(self) -> None:
        """
        This method calls the controller to sort all player instances by ranking
        """
        print('========================')
        print('All Players by ranking: ')
        print('========================')
        for player in self.current_page_ctrl().sort_by_ranking():
            print(f'- {player.last_name}, {player.first_name}, {player.identifier_pod},'
                  f' {player.birthdate_pod}, {player.gender_pod}\n'
                  f'-> {player.ranking}'
                  )
        self.current_page_ctrl().run()