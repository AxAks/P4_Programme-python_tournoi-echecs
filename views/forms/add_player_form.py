# coding=utf-8

"""
Form file for the creation of a new player in the database.
"""
from views.forms.form import Form
from views.inputs.generic_inputs import GenericInputs
from views.menus import player_menu
#from views.inputs.player_inputs import PlayerInputs
from constants import PLAYER_PROPERTIES


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Player Form',
                         previous_page=player_menu.PlayerMenu(), root_page=False, exiting_message='Leaving Form',
                         properties=PLAYER_PROPERTIES)

        specific_menu_choices = [self.add_new_player]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_new_player(self) -> dict:  # à passer en tant que add_new (générique) dans Form
        print(self.program_name, '\n', self.menu_name, '\n')
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

