# coding=utf-8

from constants import MATCH_PROPERTIES
from views.forms.form import Form
from views.generic_inputs import integer_to_float, ask_integer


class NewMatchForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=MATCH_PROPERTIES, cls=self, not_asked_properties=[])

    #  c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2), pb pour la construction de la methode ...
    def ask_player_1_id(self):  # pour le player1, puis pour le player 2
        """
        This method asks for player1's ID at the beginning of a match/round
        """
        player_nb = '1'
        return input(f'Select Player{player_nb}: ')

    def ask_player_1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        player_nb = '1'
        return self.ask_player_score(player_nb)

    def ask_player_2_id(self):   # pour le player1, puis pour le player 2
        """
        This method asks for player2's ID at the beginning of a match/round
        """
        player_nb = '2'
        return input(f'Select Player{player_nb}: ')

    def ask_player_2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        player_nb = '2'
        return self.ask_player_score(player_nb)

    def ask_player_score(self, player_nb):  # est ce que ca va pas le demander dans le formulaire ?
        choices_info = '(LOSS: 0, TIE: 0.5, WIN: 1)'
        input_info = f'Enter Player{player_nb} Score {choices_info}: '
        wrong_input = 'Invalid choice (0, 0.5 or 1), please retry...'
        valid_choices = (0, 0.5, 1)
        valid_entry = False
        while not valid_entry:
            try:
                int_input = ask_integer(input_info)
                float_input = integer_to_float(int_input)
                if float_input in valid_choices:
                    if _input == 0:
                        _input = 'LOSS'
                    elif _input == 0.5:
                        _input = 'TIE'
                    else:
                        _input = 'WIN'
                    valid_entry = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input
