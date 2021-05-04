# coding=utf-8

from datetime import date

from constants import TOURNAMENT_PROPERTIES
from controllers import list_tournaments_controller
from models.models_utils.player_manager import PlayerManager
from models.player import Player
from views.forms.generic_inputs import ask_alphanumerical_string, ask_alphabetical_string, ask_iso_date, ask_integer
from views.forms.form import Form


class NewTournamentForm(Form):
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Tournament Form',
                         previous_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         properties=TOURNAMENT_PROPERTIES,
                         cls=self, not_asked_properties=['rounds_list', 'total_results', 'not_played_yet', 'done'])
        self.start_date = None

    def ask_name(self, input_info="Enter name: ") -> str:
        """
        This method asks for a name
        """
        return ask_alphanumerical_string(input_info)

    def ask_location(self, input_info="Enter Location: ") -> str:
        """
        This method asks for a location
        """
        return ask_alphabetical_string(input_info)

    def ask_start_date(self, input_info="Enter start date (YYYY-MM-DD): ") -> date:
        """
        This method asks for a start date
        """
        _input = ask_iso_date(input_info)
        self.start_date = _input
        return _input

    def ask_end_date(self, input_info="Enter end date (YYYY-MM-DD): ") -> date:
        """
        This method asks for an end date
        """
        _input = ask_iso_date(input_info)
        while _input < self.start_date:
            print(f"End Date cannot be prior to Start Date ({self.start_date})")
            self.print_please_retry()
            _input = ask_iso_date(input_info)
        return _input

    def ask_rounds(self) -> str:
        """
        This method asks for the number of rounds for the tournament
        """
        input_info = "Enter Number of Rounds : "
        _input = ask_integer(input_info)
        return _input

    def ask_identifiers_list(self) -> dict[Player]:
        """
        This method sets the number of players for the tournament to 8
        and enables to search them in the registry
        It then returns a dict of players.
        """
        tournament_players = {}
        available_players = len(PlayerManager().list_registered_players())
        nb_players = 8
        if available_players < nb_players:
            self.print_insufficient_registered_players_for_tournament()
            self.print_to_previous_menu()
            self.previous_page_ctrl().run()
        else:
            n = 1
            while n <= nb_players:
                _input = input(f'Please, search player {n} of {nb_players} by ID: ')
                player_obj = PlayerManager().search_one(_input)
                while player_obj == {}:
                    _input = input('No Player found, please retry: ')
                    player_obj = PlayerManager().search_one(_input)
                if player_obj.identifier_pod not in tournament_players:
                    tournament_players[player_obj.identifier_pod] = player_obj
                    print(f"Player {n} added")
                    print(f"{player_obj.last_name}, "
                          f"{player_obj.first_name}: "
                          f"{player_obj.identifier_pod}")
                    n += 1
                else:
                    self.print_player_already_entered()
                    self.print_please_retry()
        return tournament_players

    def ask_time_control(self) -> str:
        """
        This method asks for the time control format of a tournament using digits for choice
        and returns the matching formatted string
        """
        valid_entry = False
        choices_info = '(1: BULLET, 2: BLITZ, 3: RAPIDE)'
        input_info = f'Enter Time Control Format {choices_info}: '
        wrong_input = 'Invalid choice (1, 2 or 3)}'
        valid_choices = (1, 2, 3)

        _input = input(input_info)
        while not valid_entry:
            try:
                _input = int(_input)
                if _input in valid_choices:
                    if _input == 1:
                        _input = 'BULLET'
                    elif _input == 2:
                        _input = 'BLITZ'
                    else:
                        _input = 'RAPIDE'
                    valid_entry = True
                else:
                    print(wrong_input)
                    self.print_please_retry()
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                self.print_please_retry()
                _input = input(input_info)
        return _input

    def ask_description(self) -> str:
        """
        This method asks for a description text
        """
        input_info = "Enter Description: "
        _input = input(input_info)
        while _input == '':
            self.print_please_retry()
            print('Description cannot be empty')
            _input = input(input_info)
        return _input
