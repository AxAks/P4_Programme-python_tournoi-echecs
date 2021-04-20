# coding=utf-8

from constants import MATCH_PROPERTIES
from views.forms.form import Form


class NewMatchForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self, tournament, player1_id, player2_id):
        super().__init__(data=tournament, form_name='New Match Form',
                         properties=MATCH_PROPERTIES, cls=self, not_asked_properties=['player1_id', 'player2_id'])
        self.player1_id = player1_id
        self.player2_id = player2_id

    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        player = self.player1_id
        return self.ask_player_score(player)

    def ask_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        player = self.player2_id
        return self.ask_player_score(player)

    def ask_player_score(self, player):
        choices_info = '(LOSS: 0, TIE: 0.5, WIN: 1)'
        input_info = f'Enter Score for Player "{player}" {choices_info}: '
        wrong_input = 'Invalid choice (0, 0.5 or 1), please retry...'
        valid_choices = (0, 0.5, 1)
        valid_entry = False
        while not valid_entry:
            try:
                _input = float(input(input_info))
                if _input in valid_choices:
                    valid_entry = True
                else:
                    print(wrong_input)
            except ValueError:
                print(wrong_input)
        return _input
