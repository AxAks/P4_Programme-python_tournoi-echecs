# coding=utf-8
from controllers import list_tournaments_controller, tournament_infos_controller
from models.models_utils.player_manager import PlayerManager
from views.menus.menu import Menu


class TournamentInfosMenu(Menu):
    """
    This class is the Menu for the management of one selected Tournament.
    It enables to display information about this tournament or update it.
    """

    def __init__(self, tournament):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournament Info Menu',
                         data=tournament,
                         root_page=False, previous_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         current_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.proceed_tournament, self.sort_players_by_last_name,
                                 self.sort_players_by_ranking, self.sort_players_by_result,
                                 self.display_rounds_and_matches, self.display_not_played_matchups]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def proceed_tournament(self) -> None:
        if self.current_page_ctrl(self.data).proceed_tournament() is None:
            print('This tournament is finished, no more rounds to play')
        self.current_page_ctrl(self.data).run()

    def sort_players_by_last_name(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by last name.
        """
        players_list = self.current_page_ctrl(self.data).sort_players_by_last_name()
        self.print_hard_separator()
        print(f'Players by last name for "{self.data.name}": ')
        self.print_hard_separator()
        for player in players_list:
            self.print_player_general_infos(player)
        self.current_page_ctrl(self.data).run()

    def sort_players_by_ranking(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by general ranking.
        """
        self.print_hard_separator()
        print(f'Players by ranking for "{self.data.name}": ')
        self.print_hard_separator()
        sorted_players = self.current_page_ctrl(self.data).sort_tournament_players_by_ranking()
        for player in sorted_players:
            self.print_player_infos_simple(player)
            self.print_player_ranking_only(player)
        self.current_page_ctrl(self.data).run()

    def sort_players_by_result(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by results.
        """
        self.print_hard_separator()
        print(f'Players by result for "{self.data.name}": ')
        self.print_hard_separator()
        players_result_list = self.current_page_ctrl(self.data).sort_players_by_result(self.data)
        if players_result_list == {}:
            self.print_no_results_yet()
        else:
            for _tuple in players_result_list:
                player = _tuple[0]
                result = _tuple[1]
                self.print_player_infos_simple(player)
                self.print_player_result(result)
                self.print_player_ranking_only(player)
        self.current_page_ctrl(self.data).run()

    def display_rounds_and_matches(self) -> None:
        """
        This method calls the controller to display the match results
        in the rounds played for the selected tournament.
        """
        rounds_list = self.current_page_ctrl(self.data).display_rounds_and_matches()
        self.print_hard_separator()
        print(f'All Rounds and Matches for "{self.data.name}": ')
        self.print_hard_separator()
        if len(rounds_list) == 0:
            self.print_no_results_yet()
        else:
            for _round in rounds_list:
                self.print_soft_separator()
                self.print_round_infos_simple(_round)
                match_n = 1
                for match in _round.matches:
                    player1_obj = PlayerManager().from_identifier_to_player_obj(match.player1_id)
                    player2_obj = PlayerManager().from_identifier_to_player_obj(match.player2_id)
                    self.print_match_result(match, player1_obj, player2_obj, match_n)
                    match_n += 1
        self.current_page_ctrl(self.data).run()

    def display_not_played_matchups(self) -> None:   # pour les tests ! est ce que je le laisse ?
        """
        This method calls the controller to display for each player
        the opponents they have not played with in the previous rounds of a given tournament
        """
        not_played_yet = self.current_page_ctrl(self.data).display_not_played_yet()
        for player in not_played_yet:
            player_obj = PlayerManager().from_identifier_to_player_obj(player)
            self.header_possible_next_matchups()
            self.print_player_infos_simple(player_obj)
            for opponent in not_played_yet[player]:
                opponent_obj = PlayerManager().from_identifier_to_player_obj(opponent)
                self.print_opponent_infos_simple(opponent_obj)
            self.print_soft_separator()
        self.current_page_ctrl(self.data).run()
