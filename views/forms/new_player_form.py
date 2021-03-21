# coding=utf-8

"""
Form file for the creation of a new player in the database.
"""

from views.forms.form import Form
from views.menus.menu import Menu  # ?

from views.general_inputs import PlayerInputs


class NewPlayerForm(Form):  # faire heriter de Menu aussi ? (fonction de navigation : back, etc)
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """
    def __init__(self):
        super().__init__()

    def add_new_player(self) -> dict:  # mettre des verifs champs par champs!
        last_name = PlayerInputs().ask_player_last_name()
        first_name = PlayerInputs().ask_player_first_name()
        birthdate = PlayerInputs().ask_player_birthdate()
        gender = PlayerInputs().ask_player_gender()
        ranking = PlayerInputs().ask_player_ranking()
        new_player_dict = {
            'last_name': last_name,
            'first_name': first_name,
            'birthdate': birthdate,
            'gender': gender,
            'ranking': ranking
        }
        return new_player_dict
        """
        print(f'\nNew Player Information\n', new_player_dict)
        player_factory = Factory(Player)
        new_player = player_factory.create(**new_player_dict)
        print(player_factory.registry)
        print(new_player.__dict__)
        return new_player
        """
