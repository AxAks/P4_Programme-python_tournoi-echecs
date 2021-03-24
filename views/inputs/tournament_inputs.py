# coding=utf-8

import re
from datetime import date
from uuid import UUID

from constants import ALPHABETICAL_STRING_RULE, ALPHA_NUMERICAL_STRING_RULE

# generic inputs
from views.inputs.generic_inputs import GenericInputs


class TournamentInputs(GenericInputs):
    """
    Class listing all possible inputs related to Tournament
    """
    def __init__(self):
        super().init()

    def ask_name(self) -> str:
        """
        This method asks for a name
        """
        input_info = "Enter name: "
        _input = input(input_info)
        while not re.match(ALPHA_NUMERICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    def ask_location(self) -> str:
        """
        This method asks for a location
        """
        input_info = "Enter Tournament Location: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    def ask_start_date(self) -> date:
        """
        This method asks for a start date
        """
        valid_date = False
        input_info = "Enter Tournament's start date (YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input

    def check_one_day_tournament(self): # est ce que je le garde ? à voir plutot dans controller
        """
        This method automatically sets the end date of a tournament to the already entered start date
        if the user indicates that it is a one-day tournament.
        The input of the end date is made easier : Yes or No
        """
        start_date = self.ask_tournament_start_date()
        valid_choice = False
        choices_info = '(1: YES, 2: NO)'
        input_info = f'Is it a one-day Tournament ? {choices_info}: '
        wrong_input = 'Invalid choice (1 or 2), please retry...'
        _input = input(input_info)
        while not valid_choice:
            try:
                _input = int(_input)
                if _input in (1, 2):
                    if _input == 1:
                        _input = start_date  # pas sûr de moi ! je veux que _input aie la valeur de start_date mais là je redemande la date de debut
                    else:
                        self.ask_tournament_end_date()  # pas sûr de moi ! la ca doit etre bon ! ca renvoie vers ask_tournament_end_date
                        valid_choice = True  # bizarre !
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
            return start_date, _input

    def ask_end_date(self) -> date:
        """
        This method asks for an end date
        """
        valid_date = False
        input_info = "Enter Tournament's end date (YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input

    def ask_identifiers_list(self) -> list:
        # liste d'UUID de Players et le nombre est fixé à 8 joueurs : nom de fonction pas explicite
        # ce serait sympa de pouvoir faire une recherche dans la base des joueurs !
        """
        This method asks for a list of 8 players for a tournament
        """
        #  mettre des verifs de formatage de l'input ici et demander de resaisir si pas bon
        # mais faire une recherche car impossible de taper un uuid4...
        tournament_players_identifier = []
        n = 1
        while n < 9:
            valid_uuid4 = False
            input_info = f"Enter Player ID {n}/8:"
            _input = input(input_info)
            # mettre en place une recherche dans le registre plutot ! integrer la fonction search_player_by_id
            while not valid_uuid4:
                try:
                    _input = UUID(str(_input), version=4)
                    valid_uuid4 = True
                    if _input not in tournament_players_identifier:
                        tournament_players_identifier.append(_input)
                        n += 1
                    else:
                        print('Identifier already entered in the list, please retry...')
                except ValueError:
                    print('Invalid player, please retry...')
                    _input = input(input_info)
        return tournament_players_identifier

    def ask_time_control(self) -> str:
        """
        This method asks for the time control format of a tournament using digits
        and returns a formatted string
        """
        valid_time_control = False
        choices_info = '(1: BULLET, 2: BLITZ, 3: RAPIDE)'
        input_info = f'Enter Time Control Format {choices_info}: '
        wrong_input = 'Invalid choice (1, 2 or 3), please retry...'
        _input = input(input_info)
        while not valid_time_control:
            try:
                _input = int(_input)
                if _input in (1, 2, 3):
                    if _input == 1:
                        _input = 'BULLET'
                    elif _input == 2:
                        _input == 'BLITZ'
                    else:
                        _input = 'RAPIDE'
                    valid_time_control = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input

    def ask_description(self) -> str:
        """
        This method asks for a description of a tournament
        """
        input_info = "Enter Tournament Description: "
        _input = input(input_info)
        while _input == '':
            print('Description cannot be empty, please retry...')
            _input = input(input_info)
        return _input
