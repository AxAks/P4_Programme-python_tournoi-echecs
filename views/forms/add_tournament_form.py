# coding=utf-8

from views.forms.form import Form
from views.inputs.get_properties import GetProperties
from constants import TOURNAMENT_PROPERTIES


class NewTournamentForm(Form):
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=TOURNAMENT_PROPERTIES)

    def add_new_tournament(self) -> dict: #  à passer en tant que add_new dans Form
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        ask_properties_dict = {}
        for _property in TOURNAMENT_PROPERTIES:
            if _property not in ('rounds_list', 'rounds'):
                ask_properties_dict[_property] = GetProperties().ask_properties(_property)

        new_tournament_dict = {}
        for key in ask_properties_dict:
            new_tournament_dict[key] = ask_properties_dict[key]
        return new_tournament_dict
