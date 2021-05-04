# coding=utf-8

class View:
    """
    This class is a parent Class for Menu and Form screens
    It enables them to  shared some common properties
    """
    def __init__(self, program_name, menu_name, data=None,
                 previous_page_ctrl=None, exiting_message='Program Terminated'):

        self.program_name = program_name
        self.menu_name = f'-{menu_name}-'
        self.data = data
        self.previous_page_ctrl = previous_page_ctrl
        self.exiting_message = exiting_message

    def general_header_menu(self):
        print('========================')
        print(self.program_name, '\n', self.menu_name)
        print('========================')

    def header_by_ranking(self):
        print(f'========================\n'
              f'All Players by ranking: \n'
              f'========================')
    def header_by_last_name(self):
        print(f'========================\n'
              f'All Players by last name: \n'
              f'========================')

    def print_hard_separator(self):
        print('========================')

    def print_soft_separator(self):
        print('')

    def input_search_a_player_by_id(self):
        input('search a player by ID: ')

    def header_player_search(self):
        print(f'========================\n'
              f'Player Search Results: \n'
              f'========================')

    def header_ranking_update(self):
        print(f'========================\n'
              f'Player Ranking Update: \n'
              f'========================')

    def print_player_general_infos(self, player):
        print(f'Player: {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
              f'More infos: {player.birthdate_pod}, {player.gender_pod}, {player.ranking}')

    def print_player_infos_simple(self, player_obj):
        print(f'Player: {player_obj.last_name}, {player_obj.first_name}, {player_obj.identifier_pod}')

    def print_player_ranking_only(self, player_obj):
        print(f'General Ranking: {player_obj.ranking}')

    def print_opponent_infos_simple(self, opponent_obj):
        print(f'Opponent: {opponent_obj.last_name}, {opponent_obj.first_name}, {opponent_obj.identifier_pod}')

    def print_tournament_general_infos(self, tournament_obj):
        print(f'Name: {tournament_obj.name}, Location {tournament_obj.location},\n'
              f'From {tournament_obj.start_date} to {tournament_obj.end_date},\n '
              f'{tournament_obj.rounds} Rounds, Time Control: {tournament_obj.time_control}\n'
              f'Description: {tournament_obj.description}')

    def print_round_infos_simple(self, round_obj):
        print(f'{round_obj.name}: from {round_obj.start_time} to {round_obj.end_time}')

    def print_no_tournament_found(self):
        print('No tournament in the registry')

    def print_no_player_found(self):
        print('No player in the registry')

    def print_no_results_yet(self):
        print('There are no Results for this Tournament yet')

    def print_match_result(self, match, player1_obj, player2_obj, match_n):
        print(f'Match {match_n}:\n'
              f'{player1_obj.last_name}, {player1_obj.first_name}, {player1_obj.identifier_pod}\n'
              f'{match.player1_score_pod}\n'
              f'{player2_obj.last_name}, {player2_obj.first_name}, {player2_obj.identifier_pod}\n'
              f'{match.player2_score_pod}\n')

    def print_please_retry(self):
        print('please retry...: ')
