# coding=utf-8

class View:
    """
    This class is a parent Class for Menu and Form screens
    It enables them to  shared some common properties
    It also groups several prints used in the child classes
    """
    def __init__(self, program_name, menu_name, data=None,
                 previous_page_ctrl=None, exiting_message='Program Terminated'):

        self.program_name = program_name
        self.menu_name = f'-{menu_name}-'
        self.data = data
        self.previous_page_ctrl = previous_page_ctrl
        self.exiting_message = exiting_message

    def print_hard_separator(self):
        print('========================')

    def print_soft_separator(self):
        print('')

    def general_header_menu(self):
        self.print_hard_separator()
        print(self.program_name, '\n', self.menu_name)
        self.print_hard_separator()

    def header_player_search(self):
        self.print_hard_separator()
        print('Player Search Results: ')
        self.print_hard_separator()

    def header_tournaments_search(self):
        self.print_hard_separator()
        print('Tournaments Search: ')
        self.print_hard_separator()

    def header_tournaments_search_results(self):
        self.print_hard_separator()
        print('Tournaments Search Results: ')
        self.print_hard_separator()

    def header_tournament_selection(self):
        self.print_hard_separator()
        print('Tournament Selection: ')
        self.print_hard_separator()

    def header_tournament_by_name(self):
        self.print_hard_separator()
        print('List of all Tournaments by Name: ')
        self.print_hard_separator()

    def header_tournament_by_start_date(self):
        self.print_hard_separator()
        print('List of all Tournaments sorted by Start Date: ')
        self.print_hard_separator()

    def header_tournament_by_location(self):
        self.print_hard_separator()
        print('List of all Tournaments by Location: ')
        self.print_hard_separator()

    def header_ranking_update(self):
        self.print_hard_separator()
        print('Player Ranking Update: ')
        self.print_hard_separator()

    def header_players_by_ranking(self):
        self.print_hard_separator()
        print('All Players by ranking: ')
        self.print_hard_separator()

    def header_players_by_last_name(self):
        self.print_hard_separator()
        print('All Players by last name: ')
        self.print_hard_separator()

    def input_search_a_player_by_id(self):
        _input =input('search a player by ID: ')
        return _input

    def input_search_a_tournament_by_name_location_dates(self):
        _input = input('Search a Tournament by Name, Location or dates : ')
        return _input

    def print_new_player_registered(self):
        print('New Player registered: ')

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

    def print_new_tournament_registered(self):
        print('New Tournament registered: ')

    def print_tournament_infos_simple(self, tournament_obj):
        print(f'Name: {tournament_obj.name}, Location {tournament_obj.location}\n'
              f'From {tournament_obj.start_date} to {tournament_obj.end_date}')

    def print_round_infos_simple(self, round_obj):
        print(f'{round_obj.name}: from {round_obj.start_time} to {round_obj.end_time}')

    def print_no_tournament_found(self):
        print('No tournament in the registry')

    def print_no_player_found(self):
        print('No player in the registry')

    def print_one_tournament_found(self):
        print('1 Tournament found in Registry for this research:')

    def print_no_results_yet(self):
        print('There are no Results for this Tournament yet')

    def print_match_result(self, match, player1_obj, player2_obj, match_n):
        print(f'Match {match_n}:\n'
              f'{player1_obj.last_name}, {player1_obj.first_name}, {player1_obj.identifier_pod}\n'
              f'{match.player1_score_pod}\n'
              f'{player2_obj.last_name}, {player2_obj.first_name}, {player2_obj.identifier_pod}\n'
              f'{match.player2_score_pod}\n')

    def print_please_confirm(self):
        print('Please confirm this information: ')

    def print_please_retry(self):
        print('Please retry...')

    def print_to_previous_menu(self):
        print('Back to previous menu page ...')

    def print_error_occured(self):
        print('An Error has occurred')

    def print_cancelled(self):
        print('Cancelled')
