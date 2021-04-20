# coding=utf-8

from constants import MATCH_PROPERTIES
from models.models_utils.player_manager import PlayerManager
from views.forms.form import Form


class NewMatchForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self, tournament):
        super().__init__(data=tournament, form_name='New Match Form', properties=MATCH_PROPERTIES, cls=self, not_asked_properties=[])

    def ask_player1_id(self):
        """
        This method enables to search player1 of a match by ID at the beginning of a match/round
        """
        tournament_players = self.list_tournament_players()
        player_nb = '1'
        message_info = f'Please, search player {player_nb}: '
        valid_search = False
        while not valid_search:
            _input = input(message_info)
            search = PlayerManager().search_one(_input)
            if search in tournament_players:
                valid_search = True
                return search
            else:
                for player in tournament_players:
                    print(player)
                print("Player not found in this tournament, choose ID from above ...")

    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        player_nb = '1'
        return self.ask_player_score(player_nb)

    def ask_player2_id(self):
        """
        This method enables to search player2 of a match by ID at the beginning of a match/round
        """
        tournament_players = self.list_tournament_players()
        player_nb = '2'
        message_info = f'Please, search player {player_nb}: '
        valid_search = False
        while not valid_search:
            _input = input(message_info)
            search = PlayerManager().search_one(_input)
            if search in tournament_players:  # pas de verif que Player 2 != de player 1 !
                valid_search = True
                return search
            else:
                print("Player not found in this tournament, please retry ...")

    def ask_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        player_nb = '2'
        return self.ask_player_score(player_nb)

    def list_tournament_players(self):
        tournament_players = []
        for uuid in self.data.identifiers_list:
            player_obj = PlayerManager().from_identifier_to_player_obj(uuid)
            tournament_players.append(player_obj)
        return tournament_players

    def ask_player_score(self, player_nb):
        choices_info = '(LOSS: 0, TIE: 0.5, WIN: 1)'
        input_info = f'Enter Player{player_nb} Score {choices_info}: '
        wrong_input = 'Invalid choice (0, 0.5 or 1), please retry...'
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
            except ValueError:
                print(wrong_input)
        return _input
