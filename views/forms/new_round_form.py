# coding=utf-8

from constants import ROUND_PROPERTIES
from controllers import tournament_infos_controller
from views.forms.form import Form
from views.forms.new_match_form import NewMatchForm


class NewRoundForm(Form):
    """
    This class asks the required data for the creation of a Round instance.
    and returns a dict.
    """

    def __init__(self, tournament):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Round Form',
                         previous_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         data=tournament,
                         properties=ROUND_PROPERTIES, cls=self, not_asked_properties=['matches', 'results'])

    # à voir
    def ask_name(self):
        """
        This method asks for the round's name at the beginning of the round
        """
        n = str(len(self.data.rounds_list) + 1)
        round_name = f'Round {n}'
        return round_name

    def ask_matches(self):
        """"
        This method asks for the list of match results for a round
        """
        round_matches = []
        n = 1
        while n <= 4:
            match = NewMatchForm(self.data).add_new()
            round_matches.append(match)
            n += 1
        return round_matches

    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !   datetime.now() quand on le créé, ou quand les joueurs ont commencé à jouer
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_start_time()

    def ask_end_time(self):  # doit etre renseigné automatiquement en fait ! datetime.now() quand on entre le resultat du dernier match
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_end_time()
