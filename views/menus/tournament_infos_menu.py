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
        print('========================')
        print(f'Players by last name for "{self.data.name}": ')
        print('========================')
        for player in players_list:
            self.print_player_general_infos(player)
        self.current_page_ctrl(self.data).run()

    def sort_players_by_ranking(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by general ranking.
        """
        print('========================')
        print(f'Players by ranking for "{self.data.name}": ')
        print('========================')
        sorted_players = self.current_page_ctrl(self.data).sort_tournament_players_by_ranking()
        for player in sorted_players:
            self.print_player_infos_simple(player)
            print(f'General Ranking: {player.ranking}')
        self.current_page_ctrl(self.data).run()

    def sort_players_by_result(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by results.
        """
        print('========================')
        print(f'Players by result for "{self.data.name}": ')
        print('========================')
        players_result_list = self.current_page_ctrl(self.data).sort_players_by_result(self.data)
        if players_result_list == {}:
            self.print_no_results_yet()
        else:
            for _tuple in players_result_list:
                PLAYER = _tuple[0]
                RESULT = _tuple[1]
                print(f"Player: {PLAYER.last_name}, {PLAYER.first_name}, {PLAYER.identifier_pod}\n"
                      f"General Ranking: {PLAYER.ranking}\n"
                      f"Total Points: {RESULT}")
        self.current_page_ctrl(self.data).run()

    def display_rounds_and_matches(self) -> None:
        """
        This method calls the controller to display the match results
        in the rounds played for the selected tournament.
        """
        rounds_list = self.current_page_ctrl(self.data).display_rounds_and_matches()
        print('========================')
        print(f'All Rounds and Matches for "{self.data.name}": ')
        print('========================')
        if len(rounds_list) == 0:
            self.print_no_results_yet()
        else:
            for _round in rounds_list:
                print(f'-> {_round.name}: from {_round.start_time} to {_round.end_time}')
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
        if not_played_yet == self.data.identifiers_list:
            self.print_no_results_yet()
        else:
            for player in not_played_yet:
                player_obj = PlayerManager().from_identifier_to_player_obj(player)
                print(f'{player_obj.last_name}, {player_obj.first_name}, {player_obj.identifier_pod}'
                      f' has never played against:')
                for opponent in not_played_yet[player]:
                    opponent_obj = PlayerManager().from_identifier_to_player_obj(opponent)
                    print(f' - {opponent_obj.last_name}, {opponent_obj.first_name}, {opponent_obj.identifier_pod}')
                print('')
        self.current_page_ctrl(self.data).run()
