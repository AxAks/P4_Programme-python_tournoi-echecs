# coding=utf-8
from controllers import list_tournaments_controller, tournament_infos_controller
from models.models_utils.player_manager import PlayerManager
from views.menus.menu import Menu


class TournamentInfosMenu(Menu):
    """
    This class is the Menu for the management of one selected Tournament.
    It enables to display informations about this tournament or update it.
    """

    def __init__(self, tournament):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournament Info Menu',
                         data=tournament,
                         root_page=False, previous_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         current_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.sort_players_by_last_name, self.sort_players_by_ranking,
                                 self.sort_players_by_result, self.display_rounds_couples,
                                 self.display_rounds_and_matches]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_players_by_last_name(self) -> None:  # for one selected tournament
        """
        This method calls the controller to display the players of the selected tournament
        sorted by last name.
        """
        players_list = self.current_page_ctrl(self.data).sort_players_by_last_name()
        print('========================')
        print(f'Players by last name for "{self.data.name}": ')
        print('========================')
        for player in players_list:
            print(f'- {player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
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
            print(f'Player: {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
                  f'General Ranking: {player.ranking}')
        self.current_page_ctrl(self.data).run()

    def sort_players_by_result(self) -> None:
        """
        This method calls the controller to display the players of the selected tournament
        sorted by results.
        """
        print('========================')
        print(f'Players by results for "{self.data.name}": ')
        print('========================')
        players_results_list = self.current_page_ctrl(self.data).sort_players_by_result(self.data)  # liste de tuples
        if players_results_list == {}:
            print("There are no Results for this Tournament yet")
        else:
            for _tuple in players_results_list:
                PLAYER = _tuple[0]
                RESULT = _tuple[1]
                print(f"Player: {PLAYER.last_name}, {PLAYER.first_name}, {PLAYER.identifier_pod}\n"
                      f"General Ranking: {PLAYER.ranking}\n"
                      f"Total Points: {RESULT}")
        self.current_page_ctrl(self.data).run()

    def display_rounds_couples(self) -> None:
        """
        This method calls the controller to display the generate player matchups
        for the different rounds of the tournament
        """
        round_pairs = self.current_page_ctrl(self.data).display_rounds_couples()  # pb de savegarde des tuples dans serialize pas géré par json !!
        r = 1
        for pairs in round_pairs:
            print(f'Round {str(r)}\n')
            m = 1
            for pair in pairs:
                print(f'Match {str(m)}\n'
                      f'Player 1: {pair[0].last_name}, {pair[0].first_name}, {pair[0].identifier_pod}\n'
                      f'Player 2: {pair[1].last_name}, {pair[1].first_name}, {pair[1].identifier_pod}\n')
                m += 1
            r += 1
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
            print('No registered Rounds for this Tournament yet')
        else:
            for _round in rounds_list:
                print(f'-> {_round.name}: from {_round.start_time} to {_round.end_time}')
                n = 1
                for match in _round.matches:
                    player1_obj = PlayerManager().from_identifier_to_player_obj(match.player1_id)
                    player2_obj = PlayerManager().from_identifier_to_player_obj(match.player2_id)
                    print(f'\nMatch {n}:\n'
                          f'- {player1_obj.identifier_pod}\n'
                          f'{player1_obj.last_name}, {player1_obj.first_name}: '
                          f'{match.player1_score_pod}\n'
                          f'- {player2_obj.identifier_pod}\n'
                          f'{player2_obj.last_name}, {player2_obj.first_name}: '
                          f'{match.player2_score_pod}\n')
                    n += 1
        self.current_page_ctrl(self.data).run()
