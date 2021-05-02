# coding=utf-8

from controllers import players_controller, home_controller
from views.menus.menu import Menu


class PlayersMenu(Menu):
    """
    This class is the Menu for Player management.
    """

    def __init__(self):

        super().__init__(program_name='Chess Tournament Manager', menu_name='Players Menu',
                         root_page=False, previous_page_ctrl=home_controller.HomeCtrl,
                         current_page_ctrl=players_controller.PlayersCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.add_player, self.update_player_ranking, self.search_by_id,
                                 self.display_by_last_name, self.display_by_ranking]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_player(self) -> None:
        """
        This method calls the controller to create a player instance
        """
        player = self.current_page_ctrl().add_player()
        print(f'New Player registered:\n'
              f'{player.last_name}, {player.first_name},\n'
              f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}, {player.identifier_pod}')
        self.current_page_ctrl().run()

    def update_player_ranking(self) -> None:
        """
        This method calls the controller to manually update a player's ranking
        """
        print('========================')
        search = input('search a player by ID: ')
        result = self.current_page_ctrl().update_player_ranking(search)
        print('========================')
        print('Player Ranking Update: ')
        print('========================')
        if isinstance(result, list):
            print('No Player found for this request, please retry')
        else:
            print(f'Ranking Updated for\n'
                  f'{result.identifier_pod}, {result.last_name}, {result.first_name}\n'
                  f'New Ranking: {result.ranking}')
        self.current_page_ctrl().run()

    def search_by_id(self) -> None:
        """
        This method calls the controller to find one or more player instances in the registry
        """
        print('========================')
        search = input('search a player by ID: ')
        players = self.current_page_ctrl().search_by_id(search)
        print('========================')
        print('Player Search Results: ')
        print('========================')
        if len(players) == 0:
            print('No Player found for this request')
        else:
            for player in players:
                print(f'{player.identifier_pod}, {player.last_name}, {player.first_name}\n'
                      f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        self.current_page_ctrl().run()

    def display_by_last_name(self) -> None:
        """
        This method calls the controller to sort all player instances by last name
        """
        print('========================')
        print('All Players by last name: ')
        print('========================')
        for player in self.current_page_ctrl().sort_by_last_name():
            print(f'- {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        self.current_page_ctrl().run()

    def display_by_ranking(self) -> None:
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
