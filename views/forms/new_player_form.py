# coding=utf-8

from datetime import date

from constants import PLAYER_PROPERTIES, RANKING_RANGE

from views.forms.form import Form
from views.generic_inputs import ask_alphabetical_string, ask_iso_date


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=PLAYER_PROPERTIES, cls=self, not_asked_properties=['identifier'])

    def ask_last_name(self, input_info="Enter Last Name: ") -> str:
        """
        This method asks for the player's last name
        and checks the formatting of the string
        """
        return ask_alphabetical_string(input_info)

    def ask_first_name(self, input_info="Enter First Name: ") -> str:
        """
        This method asks for the player's first name
        and checks the formatting of the string
        """
        return ask_alphabetical_string(input_info)

    def ask_birthdate(self, input_info="Enter Player Birthdate(YYYY-MM-DD): ") -> date:
        """
        This method asks for the player's birthdate,
        checks the format of the string entered
        and forces it into a date format
        """
        return ask_iso_date(input_info)

    def ask_gender(self) -> str:
        """
        This method asks for the player's gender using digits
        and returns a formatted string
        """
        valid_entry = False
        choices_info = '(1: MALE, 2: FEMALE)'
        input_info = f'Enter Player Gender {choices_info}: '
        wrong_input = 'Invalid choice (1 or 2), please retry...'
        valid_choices = (1, 2)

        _input = input(input_info)
        while not valid_entry:
            try:
                _input = int(_input)
                if _input in valid_choices:
                    if _input == 1:
                        _input = 'MALE'
                    else:
                        _input = 'FEMALE'
                    valid_entry = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input

    def ask_ranking(self) -> int:
        """
        This method asks a ranking between 100 and 3000
        """
        valid_entry = False
        input_info = "Enter Player Ranking: "
        wrong_input = 'Ranking must be a digit between 100 and 3000, please retry...'
        while valid_entry is False:
            try:
                _input = int(input(input_info))
                if _input in RANKING_RANGE:
                    valid_entry = True
                else:
                    print(wrong_input)
            except ValueError:
                print(wrong_input)
        return _input
