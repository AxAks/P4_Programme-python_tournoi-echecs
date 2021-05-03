# coding=utf-8

from constants import ROUND_PROPERTIES
from controllers import tournament_infos_controller
from views.forms.form import Form


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

    def ask_name(self):
        """
        This method asks for the round's name at the beginning of the round
        """
        n = str(len(self.data.rounds_list) + 1)
        round_name = f'Round {n}'
        return round_name

    def ask_start_time(self):
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_round_start_time()

    def ask_end_time(self):
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_round_end_time()
