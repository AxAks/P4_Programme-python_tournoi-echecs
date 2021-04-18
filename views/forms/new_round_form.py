# coding=utf-8

from constants import ROUND_PROPERTIES
from controllers import tournament_infos_controller
from views.forms.form import Form
from views.forms.generic_inputs import ask_alphanumerical_string


class NewRoundForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self, tournament):
        super().__init__(data=tournament, properties=ROUND_PROPERTIES, cls=self, not_asked_properties=[])

    # à voir
    def ask_name(self, input_info="Enter name: "):
        # Comme la methode de Tournament !!!! #  si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        return ask_alphanumerical_string(input_info)

    def ask_matches(self):
        # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés //controller
        """"
        This method asks for the list of match results for a round
        """
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_match_to_round()

    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_start_time()

    def ask_end_time(self):  # doit etre renseigné automatiquement en fait !
        return tournament_infos_controller.TournamentInfosCtrl(self.data).add_end_time()
