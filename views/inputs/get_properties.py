# coding=utf-8

from datetime import date

from models.models_utils import player_manager
from views.inputs.generic_inputs import ask_alphabetical_string, ask_alphanumerical_string, ask_iso_date


class GetProperties:
    """
    Class used in the forms for the input an registering of a new instance.
    """

    # et également ask_identifier ou search_by_id dans player_inputs


    #  pas ici, dans un controller !!
    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass
