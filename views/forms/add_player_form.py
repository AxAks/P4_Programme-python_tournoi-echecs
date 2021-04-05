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
                         previous_page=player_menu.PlayerMenu(), properties=PLAYER_PROPERTIES,
                         root_page=False, exiting_message='Leaving Form')
        # Utiliser super() pour remonter les attributs du dict

        specific_menu_choices = [self.add_new_player]
        [self.choices.append(choice) for choice in specific_menu_choices]


    def add_new_player(self) -> dict:  # à passer en tant que add_new (générique) dans Form
        print(self.program_name, '\n', self.menu_name, '\n')

        """
        print(f'\nNew Player Information\n', new_player_dict)  # pas dans les views
        new_player = Factory(Player).create(**new_player_dict)
        return new_player
        """

