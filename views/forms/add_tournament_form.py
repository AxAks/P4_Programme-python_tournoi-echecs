# coding=utf-8

from datetime import date

from constants import TOURNAMENT_PROPERTIES

from models.models_utils import player_manager, data
from views.inputs.generic_inputs import ask_alphanumerical_string, ask_alphabetical_string, ask_iso_date
from views.forms.form import Form


class NewTournamentForm(Form):
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=TOURNAMENT_PROPERTIES, cls=self)

    def add_new_tournament(self) -> dict: #  à passer en tant que add_new dans Form
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        new_tournament_dict = {}
        for _property in self.properties:
            if _property not in ('rounds_list', 'rounds'):
                new_tournament_dict[_property] = self.ask_property(_property)
        return new_tournament_dict

    def ask_name(self, input_info="Enter name: ") -> str:
        """
        This method asks for a name
        """
        return ask_alphanumerical_string(input_info)

    def ask_location(self, input_info = "Enter Location: ") -> str:
        """
        This method asks for a location
        """
        return ask_alphabetical_string(input_info)

    def ask_start_date(self, input_info="Enter start date (YYYY-MM-DD): ") -> date:
        """
        This method asks for a start date
        """
        return ask_iso_date(input_info)

    def ask_end_date(self, input_info="Enter end date (YYYY-MM-DD): ") -> date:
        """
        This method asks for an end date
        """
        return ask_iso_date(input_info)

    def ask_identifiers_list(self) -> list: # pas generique actuellement...!
        # liste d'UUID de Players et le nombre est fixé à 8 joueurs : mal nommée non explicite
        """
        This method asks for a list of 8 players for a tournament
        """
        tournament_players_identifier = {}
        n = 1
        print("Please, select players to add")
        while n < 9:
            player_dict = player_manager.search_one_player()
            for key in player_dict:
                if str(key) not in tournament_players_identifier: # pb il accepte les doublons de joueurs, la verif ne fonctionne plus
                    tournament_players_identifier[str(key)] = player_dict[key]
                    print(f"Player {n}/8 added")
                    print(f"{player_dict[key].last_name}, "
                          f"{player_dict[key].first_name}: "
                          f"{player_dict[key].identifier_pod}")
                    n += 1
                else:
                    print('Player already entered in the list, please retry...')
        return tournament_players_identifier

    def ask_time_control(self) -> str:
        """
        This method asks for the time control format of a tournament using digits for choice
        and returns the matching formatted string
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
        return _input  # retourne "2" au lieu de BLITZ (l'int au lieu du str)

    def ask_description(self) -> str:
        """
        This method asks for a description text
        """
        input_info = "Enter Description: "
        _input = input(input_info)
        while _input == '':
            print('Description cannot be empty, please retry...')
            _input = input(input_info)
        return _input

