# coding=utf-8

from constants import MATCH_PROPERTIES
from views.forms.form import Form


class NewMatchForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self, tournament):
        super().__init__(data=tournament, properties=MATCH_PROPERTIES, cls=self, not_asked_properties=[])

    #  c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2), pb pour la construction de la methode ...
    def ask_player1_id(self):  # pour le player1, puis pour le player 2
        """
        This method asks for player1's ID at the beginning of a match/round
        """
        player_nb = '1'
        return input(f'Select Player{player_nb}: ')

    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        player_nb = '1'
        return self.ask_player_score(player_nb)

    def ask_player2_id(self):   # pour le player1, puis pour le player 2
        """
        This method asks for player2's ID at the beginning of a match/round
        """
        player_nb = '2'
        return input(f'Select Player{player_nb}: ')

    def ask_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        player_nb = '2'
        return self.ask_player_score(player_nb)

    def ask_player_score(self, player_nb):
        choices_info = '(LOSS: 0, TIE: 1, WIN: 2)'
        input_info = f'Enter Player{player_nb} Score {choices_info}: '
        wrong_input = 'Invalid choice (0, 1 or 2), please retry...'
        valid_choices = (0, 0.5, 1)
        valid_entry = False
        while not valid_entry:
            try:
                _input = float(input(input_info))
                if _input in valid_choices:
                    if _input == 0:
                        _input = 'LOSS'
                        valid_entry = True
                    elif _input == 0.5:
                        _input = 'TIE'
                        valid_entry = True
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
