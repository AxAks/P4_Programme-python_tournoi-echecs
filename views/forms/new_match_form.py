# coding=utf-8

from constants import MATCH_PROPERTIES
from controllers import tournament_infos_controller
from views.forms.form import Form


class NewMatchForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self, tournament, player1_id, player2_id):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Match Form',
                         previous_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         data=tournament,
                         properties=MATCH_PROPERTIES, cls=self, not_asked_properties=[])
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.player1_score = None

    def ask_player1_id(self):
        """
        This method returns player1's id for a given match for confirmation
        """
        return self.player1_id

    def ask_player2_id(self):
        """
        This method returns player2's id for a given match for confirmation
        """
        return self.player2_id

    def ask_player1_score(self):
        """
        This method asks for player1's score
        """
        self.player1_score = self.ask_players_scores()
        return self.player1_score

    def ask_player2_score(self):
        """
        This method automatically calculates and returns player2's score for confirmation
        """
        player1_score = self.player1_score
        player2_score = 1 - player1_score
        return player2_score

    def ask_players_scores(self):
        choices_info = '(LOSS: 0, TIE: 0.5, WIN: 1)'
        input_info = f'Enter Score for Player1 ({self.player1_id}) {choices_info}: '
        wrong_input = 'Invalid choice (0, 0.5 or 1)'
        valid_choices = (0, 0.5, 1)
        valid_entry = False
        while not valid_entry:
            try:
                _input = float(input(input_info))
                if _input in valid_choices:
                    valid_entry = True
                else:
                    print(wrong_input)
                    self.print_please_retry()
            except ValueError:
                print(wrong_input)
                self.print_please_retry()
        return _input
