# coding=utf-8

"""
import re
from datetime import date
from uuid import UUID

from constants import ALPHABETICAL_STRING_RULE, RANKING_RANGE

from models.factory import Factory
from views.inputs import GenericInputs


class PlayerInputs(GenericInputs):
"""
    #Class listing all possible inputs related to players
"""
    def __init__(self):
        super().__init__()

    @property
    def ask_last_name(self) -> str:
"""
        #This method asks for the player's last name
        #and checks the formatting of the string
"""
        input_info = f"Enter Last Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_first_name(self) -> str:
"""
        #This method asks for the player's first name
        #and checks the formatting of the string
"""
        input_info = "Enter First Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input


    def search_by_id(self, _obj, search): # _obj = Tournament ou Player: sachant que ce n'est pas le meme type d'ID... (Round et Match ? ils n'ont pas d'ID mais on peut en faire voir si utile)
        # probleme, je ne sais pas comment faire avec le player_registry, l'idée est de chercher l'uuid dans le dict player_registry ou l'identifier du tournoi dans tournament_registry
        Factory(_obj).search(search)  # pas

    @property
    def ask_identifier(self) -> str:  # pas facile de copier un uuid4 , plutot une recherche !! # juste pour Player !
        valid_uuid4 = False
        input_info = f"Enter Player ID:"
        _input = input(input_info)
        while not valid_uuid4:
            try:
                _input = UUID(str(_input), version=4)
                valid_uuid4 = True
            except ValueError:
                print('Invalid player Identifier, please retry...')
                _input = input(input_info)
        return _input

    @property
    def ask_birthdate(self) -> date:
"""
        #This method asks for the player's birthdate,
        #checks the format of the string entered
        #and forces it into a date format
"""
        valid_date = False
        input_info = "Enter Player Birthdate(YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input

    @property
    def ask_gender(self) -> str:
"""
        #This method asks for the player's gender using digits
        #and returns a formatted string
"""
        valid_gender = False
        choices_info = '(1: MALE, 2: FEMALE)'
        input_info = f'Enter Player Gender {choices_info}: '
        wrong_input = 'Invalid choice (1 or 2), please retry...'

        _input = input(input_info)
        while not valid_gender:
            try:
                _input = int(_input)
                if _input in (1, 2):
                    if _input == 1:
                        _input = 'MALE'
                    else:
                        _input = 'FEMALE'
                    valid_gender = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input

    @property
    def ask_ranking(self) -> int:
"""
        #This method asks for the player's ranking
"""
        valid_ranking = False
        input_info = "Enter Player Ranking: "
        wrong_input = 'Ranking must be a digit between 100 and 3000, please retry...'
        while valid_ranking is False:
            try:
                _input = int(input(input_info))
                if _input in RANKING_RANGE:
                    valid_ranking = True
                else:
                    print(wrong_input)
            except ValueError:
                print(wrong_input)
        return _input
"""