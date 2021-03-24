# coding=utf-8

"""
Generic Class for Forms
"""

from views.menus.menu import Menu
from views.inputs.generic_inputs import GenericInputs


class Form(Menu):
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """
    def __init__(self, program_name, menu_name, previous_page, root_page, exiting_message):
        super().__init__(program_name=program_name, menu_name=menu_name,
                         previous_page=previous_page, root_page=root_page,
                         exiting_message=exiting_message)

    def add_new(self, properties) -> dict:   # essayer de rendre add_new_tournament et add_new_player générique !! cf ask_obj_property() dans class Player_Inputs
        print(self.program_name, '\n', self.menu_name, '\n')
        # Où est ce que je recupère la liste des properties et comment je fais le tri par rapport à l'objet, à continuer elaboration/redaction!
         # reflechir par rapport à add tournament et add player
        # properties = ['last_name', 'first_name', 'birthdate', 'gender', 'ranking']
        # cette partie est valable, mais ask_property pas codée
        properties_dict = {}
        for _property in properties:
            properties_dict[_property] = GenericInputs().ask_property()
        print(properties)
        return properties_dict
        """
        # Ex de properties pour un objet: 
        # 'last_name', 
        # 'first_name', 
        # 'birthdate', 
        # 'gender', 
        # 'ranking'
        # Ex de fonctions d'input correspondantes pour cet objet:
        # PlayerInputs().ask_player_last_name(),   # PlayerInputs doit aussi etre rendu iddentique poru tous les objects
        # PlayerInputs().ask_player_first_name(),
        # PlayerInputs().ask_player_birthdate(),
        # PlayerInputs().ask_player_gender(),
        # PlayerInputs().ask_player_ranking()
        """
