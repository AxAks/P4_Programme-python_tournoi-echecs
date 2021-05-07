# coding=utf-8

from datetime import date, timedelta

from constants import PLAYER_PROPERTIES, RANKING_RANGE, MINIMUM_AGE
from controllers import players_controller

from views.forms.form import Form
from views.forms.generic_inputs import ask_alphabetical_string, ask_iso_date


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Player Form',
                         previous_page_ctrl=players_controller.PlayersCtrl,
                         properties=PLAYER_PROPERTIES, cls=self,
                         not_asked_properties=['identifier'])

    def ask_last_name(self, input_info="Enter Last Name: ") -> str:
        """
        This method asks for the player's last name
        and checks the formatting of the string
        """
        self.print_hard_separator()
        return ask_alphabetical_string(input_info)

    def ask_first_name(self, input_info="Enter First Name: ") -> str:
        """
        This method asks for the player's first name
        and checks the formatting of the string
        """
        self.print_hard_separator()
        return ask_alphabetical_string(input_info)

    def ask_birthdate(self, input_info="Enter Player Birthdate(YYYY-MM-DD): ") -> date:
        """
        This method asks for the player's birthdate,
        checks the format of the string entered
        and forces it into a date format
        It also checks that the player is over 12
        """
        wrong_input = 'Players must be at least 12 year old'
        self.print_hard_separator()
        _input = ask_iso_date(input_info)
        while date.today() - _input < timedelta(days=MINIMUM_AGE * 365):
            print(wrong_input)
            self.print_please_retry()
            self.print_hard_separator()
            _input = ask_iso_date(input_info)
        return _input

    def ask_gender(self) -> str:
        """
        This method asks for the player's gender using digits
        and returns a formatted string
        """
        valid_entry = False
        choices_info = '(1: MALE, 2: FEMALE)'
        input_info = f'Enter Player Gender {choices_info}: '
        wrong_input = 'Invalid choice (1 or 2)'
        valid_choices = (1, 2)

        self.print_hard_separator()
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
                    self.print_please_retry()
                    self.print_hard_separator()
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                self.print_please_retry()
                self.print_hard_separator()
                _input = input(input_info)
        return _input

    def ask_ranking(self) -> int:
        """
        This method asks a ranking between 100 and 3000
        """
        valid_entry = False
        input_info = 'Enter Player Ranking (from 100 to 3000): '
        wrong_input = 'Ranking must be a digit between 100 and 3000'
        while not valid_entry:
            try:
                self.print_hard_separator()
                _input = int(input(input_info))
                if _input in RANKING_RANGE:
                    valid_entry = True
                else:
                    print(wrong_input)
                    self.print_please_retry()
            except ValueError:
                print(wrong_input)
                self.print_please_retry()
        return _input
