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

    @staticmethod
    def print_hard_separator():
        print('========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================'
              '========================')

    @staticmethod
    def print_soft_separator():
        print('')

    @staticmethod
    def print_new_player_registered(info: str = 'New Player registered: '):
        print(info)

    @staticmethod
    def print_update_rankings(info: str = 'Please update Players Rankings'):
        print(info)

    @staticmethod
    def print_new_tournament_registered(info: str = 'New Tournament registered: '):
        print(info)

    @staticmethod
    def print_new_round_registered(info: str = 'New Round registered: '):
        print(info)

    @staticmethod
    def print_new_match_registered(info: str = 'New Match registered: '):
        print(info)

    @staticmethod
    def print_no_tournament_found(info: str = 'No tournament found'):
        print(info)

    @staticmethod
    def print_no_player_found(info: str = 'No player found'):
        print(info)

    @staticmethod
    def print_player_already_entered(info: str = 'Player already entered'):
        print(info)

    @staticmethod
    def print_all_players_have_played(info: str = 'All players have played together'):
        print(info)

    @staticmethod
    def print_one_tournament_found(info: str = '1 Tournament found in Registry for this research:'):
        print(info)

    @staticmethod
    def print_nb_rounds_tournament(nb_rounds_total: int):
        print(f'This is a tournament in {nb_rounds_total} rounds')

    @staticmethod
    def print_nb_rounds_played(nb_rounds_played: int):
        print(f'Latest round played is round {nb_rounds_played}')

    @staticmethod
    def print_no_rounds_played_yet():
        print(f'No round have been played yet')

    @staticmethod
    def print_no_results_yet(info: str = 'There are no Results for this Tournament yet'):
        print(info)

    @staticmethod
    def print_please_confirm(info: str = 'Please confirm this information: '):
        print(info)

    @staticmethod
    def print_please_retry(info: str = 'Please retry...'):
        print(info)

    @staticmethod
    def print_to_previous_menu(info: str = 'Back to previous menu page ...'):
        print(info)

    @staticmethod
    def print_error_occurred(info: str = 'An Error has occurred'):
        print(info)

    @staticmethod
    def print_cancelled(info: str = 'Cancelled'):
        print(info)

    @staticmethod
    def print_insufficient_registered_players_for_tournament():
        print('Not enough players in the registry')
        print('Please create more players players')

    @staticmethod
    def print_player_general_infos(player):
        print(f'Player: {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
              f'- birthdate: {player.birthdate_pod}, gender: {player.gender_pod}, ranking: {player.ranking}')

    @staticmethod
    def print_player_infos_simple(player_obj):
        print(f'Player: {player_obj.last_name}, {player_obj.first_name}, {player_obj.identifier_pod}')

    @staticmethod
    def print_player_ranking_only(player_obj):
        print(f'General Ranking: {player_obj.ranking}')

    @staticmethod
    def print_player_result(result):
        print(f"Total Points in Tournament: {result}")

    @staticmethod
    def print_opponent_infos_simple(opponent_obj):
        print(f'- Opponent: {opponent_obj.last_name}, {opponent_obj.first_name}, {opponent_obj.identifier_pod}')

    @staticmethod
    def print_tournament_with_descr(tournament_obj):
        print(f'Name: "{tournament_obj.name}" '
              f'from {tournament_obj.start_date} to {tournament_obj.end_date} in {tournament_obj.location} '
              f'({tournament_obj.time_control_pod}: {tournament_obj.rounds} Rounds, '
              f'{len(tournament_obj.identifiers_list)} Players)\n'
              f'- Description: "{tournament_obj.description}"')

    @staticmethod
    def print_tournament_no_descr(tournament_obj):
        print(f'Name: "{tournament_obj.name}" '
              f'from {tournament_obj.start_date} to {tournament_obj.end_date} in {tournament_obj.location} '
              f'({tournament_obj.time_control_pod}: {tournament_obj.rounds} Rounds, '
              f'{len(tournament_obj.identifiers_list)} Players)')

    @staticmethod
    def print_round_infos_simple(round_obj):
        print(f'-> {round_obj.name}: from {round_obj.start_time} to {round_obj.end_time} <-')

    @staticmethod
    def print_matchup(player_obj_1, player_obj_2, matchup_n):
        print(f'Matchup {matchup_n}:\n'
              f'- Player 1: {player_obj_1.last_name}, {player_obj_1.first_name}, {player_obj_1.identifier_pod}\n'
              f'- Player 2: {player_obj_2.last_name}, {player_obj_2.first_name}, {player_obj_2.identifier_pod}')

    @staticmethod
    def print_match_result(match, player1_obj, player2_obj, match_n):
        print(f'Match {match_n}:\n'
              f'- Score: {match.player1_score_pod}, {player1_obj.last_name}, {player1_obj.first_name},'
              f' {player1_obj.identifier_pod}\n'
              f'- Score: {match.player2_score_pod}, {player2_obj.last_name}, {player2_obj.first_name},'
              f' {player2_obj.identifier_pod}')

    @staticmethod
    def input_search_a_player_by_id():
        _input = input('Search a player by ID: ')
        return _input

    @staticmethod
    def input_search_a_tournament_by_name_location_dates():
        _input = input('Search a Tournament by Name, Location or dates : ')
        return _input
