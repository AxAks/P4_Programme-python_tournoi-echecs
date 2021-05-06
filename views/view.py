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
        print('========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================')

    def print_soft_separator(self):
        print('')

    def general_header_menu(self):
        self.print_hard_separator()
        print(self.program_name, '\n', self.menu_name)
        self.print_hard_separator()

    def specific_header_menu(self, header_name: str):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_player_search(self, header_name: str = 'Players Search '):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_player_search_results(self, header_name: str = 'Player Search Results'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournaments_search(self, header_name: str = 'Tournaments Search'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournaments_search_results(self, header_name: str = 'Tournaments Search Results'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournament_selection(self, header_name: str = 'Tournament Selection'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournament_by_name(self, header_name: str = 'List of all Tournaments by Name'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournament_by_start_date(self, header_name: str = 'List of all Tournaments sorted by Start Date'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournament_by_location(self, header_name: str = 'List of all Tournaments by Location'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_tournament_player_ranking_update(self, header_name: str = 'After Tournament New Player Rankings'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_possible_next_matchups(self, header_name: str = 'Remaining Possible Matchups'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_general_player_ranking_update(self, header_name: str = 'Player Ranking Update'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_players_by_ranking(self, header_name: str = 'All Players by ranking'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def header_players_by_last_name(self, header_name: str = 'All Players by last name'):
        self.print_hard_separator()
        print(header_name)
        self.print_hard_separator()

    def print_new_player_registered(self, info: str = 'New Player registered: '):
        print(info)

    def print_update_rankings(self, info: str = 'Please update Players Rankings'):
        print(info)

    def print_new_tournament_registered(self, info: str = 'New Tournament registered: '):
        print(info)

    def print_no_tournament_found(self, info: str = 'No tournament found'):
        print(info)

    def print_no_player_found(self, info: str = 'No player found'):
        print(info)

    def print_player_already_entered(self, info: str = 'Player already entered'):
        print(info)

    def print_all_players_have_played(self, info: str = 'All players have played together'):
        print(info)

    def print_one_tournament_found(self, info: str = '1 Tournament found in Registry for this research:'):
        print(info)

    def print_no_results_yet(self, info: str = 'There are no Results for this Tournament yet'):
        print(info)

    def print_please_confirm(self, info: str = 'Please confirm this information: '):
        print(info)

    def print_please_retry(self, info: str = 'Please retry...'):
        print(info)

    def print_to_previous_menu(self, info: str = 'Back to previous menu page ...'):
        print(info)

    def print_error_occured(self, info: str = 'An Error has occurred'):
        print(info)

    def print_cancelled(self, info: str = 'Cancelled'):
        print(info)


    def print_insufficient_registered_players_for_tournament(self):
        print('Not enough players in the registry')
        print('Please create more players players')

    def print_player_general_infos(self, player):
        print(f'Player: {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
              f'- birthdate: {player.birthdate_pod}, gender: {player.gender_pod}, ranking: {player.ranking}')

    def print_player_infos_simple(self, player_obj):
        print(f'Player: {player_obj.last_name}, {player_obj.first_name}, {player_obj.identifier_pod}')

    def print_player_ranking_only(self, player_obj):
        print(f'General Ranking: {player_obj.ranking}')

    def print_player_result(self, result):
        print(f"Total Points in Tournament: {result}")

    def print_opponent_infos_simple(self, opponent_obj):
        print(f'Opponent: {opponent_obj.last_name}, {opponent_obj.first_name}, {opponent_obj.identifier_pod}')

    def print_tournament_general_infos(self, tournament_obj):
        print(f'Name: {tournament_obj.name}, Location: {tournament_obj.location},\n'
              f'From {tournament_obj.start_date} to {tournament_obj.end_date},\n '
              f'{tournament_obj.rounds} Rounds, Time Control: {tournament_obj.time_control}\n'
              f'Description: {tournament_obj.description}')

    def print_tournament_infos_simple(self, tournament_obj):
        print(f'Name: {tournament_obj.name}, Location {tournament_obj.location}\n'
              f'From {tournament_obj.start_date} to {tournament_obj.end_date}')

    def print_round_infos_simple(self, round_obj):
        print(f'{round_obj.name}: from {round_obj.start_time} to {round_obj.end_time}')

    def print_match_result(self, match, player1_obj, player2_obj, match_n):
        print(f'Match {match_n}:\n'
              f'- Score: {match.player1_score_pod}, {player1_obj.last_name}, {player1_obj.first_name},'
              f' {player1_obj.identifier_pod}\n'
              f'- Score: {match.player2_score_pod}, {player2_obj.last_name}, {player2_obj.first_name},'
              f' {player2_obj.identifier_pod}')


    def input_search_a_player_by_id(self):
        _input =input('Search a player by ID: ')
        return _input

    def input_search_a_tournament_by_name_location_dates(self):
        _input = input('Search a Tournament by Name, Location or dates : ')
        return _input