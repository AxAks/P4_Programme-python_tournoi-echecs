# coding=utf-8

"""
Form file for the creation of a new player in the database.
"""
from views.forms.form import Form
from views.inputs.generic_inputs import GenericInputs
#from views.inputs.player_inputs import PlayerInputs
from constants import PLAYER_PROPERTIES


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """
    def __init__(self):
        super().__init__(properties=PLAYER_PROPERTIES)

    def add_new_player(self) -> dict:  # à passer en tant que add_new (générique) dans Form
        ask_properties_dict = {}
        for _property in PLAYER_PROPERTIES:
            if _property != 'identifier':
                ask_properties_dict[_property] = GenericInputs().ask_properties(_property)
            else:
                continue
        new_player_dict = {}
        for key in ask_properties_dict:
            new_player_dict[key] = ask_properties_dict[key]
        return new_player_dict

