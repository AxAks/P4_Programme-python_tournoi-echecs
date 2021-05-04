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
        specific_menu_choices = [self.add_player, self.update_player_ranking, self.display_by_last_name,
                                 self.display_by_ranking, self.search_by_id]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_player(self) -> None:
        """
        This method calls the controller to create a player instance
        """
        player = self.current_page_ctrl().add_player()
        self.print_new_player_registered()
        self.print_player_general_infos(player)
        self.current_page_ctrl().run()

    def update_player_ranking(self) -> None:
        """
        This method calls the controller to manually update a player's ranking
        """
        self.header_general_player_ranking_update()
        search = self.input_search_a_player_by_id()
        result = self.current_page_ctrl().update_player_ranking(search)
        self.header_general_player_ranking_update()
        if isinstance(result, list):
            self.print_no_player_found()
            self.print_please_retry()
        else:
            print('Ranking Updated for')
            self.print_player_infos_simple(result)
            print(f'New Ranking: {result.ranking}')
        self.current_page_ctrl().run()

    def search_by_id(self) -> None:
        """
        This method calls the controller to find one or more player instances in the registry
        """
        self.header_player_search()
        search = self.input_search_a_player_by_id()
        players = self.current_page_ctrl().search_by_id(search)
        self.header_player_search_results()
        if len(players) == 0:
            self.print_no_player_found()
        else:
            for player in players:
                self.print_player_general_infos(player)
        self.current_page_ctrl().run()

    def display_by_last_name(self) -> None:
        """
        This method calls the controller to sort all player instances by last name
        """
        self.header_players_by_last_name()
        players_list = self.current_page_ctrl().sort_by_last_name()
        if len(players_list) == 0:
            self.print_no_player_found()
        else:
            for player in players_list:
                self.print_player_general_infos(player)
            self.current_page_ctrl().run()

    def display_by_ranking(self) -> None:
        """
        This method calls the controller to sort all player instances by ranking
        """
        self.header_players_by_ranking()
        players_list = self.current_page_ctrl().sort_by_ranking()
        if len(players_list) == 0:
            self.print_no_player_found()
        else:
            for player in players_list:
                self.print_player_general_infos(player)
        self.current_page_ctrl().run()
