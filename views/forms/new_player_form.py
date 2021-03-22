# coding=utf-8

"""
Form file for the creation of a new player in the database.
"""
from views.forms.form import Form
from views.menus.menu import Menu  # ?
from views.general_inputs import PlayerInputs


class NewPlayerForm(Form, Menu):  # faire heriter de Menu aussi ? (fonction de navigation : back, etc) # en cascade actuellement : Menu -> Form -> .
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Player Form')
        specific_menu_choices = [self.add_new_player]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_new_player(self) -> dict:
        print(self.program_name, '\n', self.menu_name, '\n')
        ask_properties_dict = {
        'last_name': PlayerInputs().ask_player_last_name(),
        'first_name': PlayerInputs().ask_player_first_name(),
        'birthdate': PlayerInputs().ask_player_birthdate(),
        'gender': PlayerInputs().ask_player_gender(),
        'ranking': PlayerInputs().ask_player_ranking()
        }
        new_player_dict = {}
        for key in ask_properties_dict:
            new_player_dict[key] = ask_properties_dict[key]
        return new_player_dict
        """
        print(f'\nNew Player Information\n', new_player_dict)  # pas dans les views
        new_player = Factory(Player).create(**new_player_dict)
        return new_player
        """
