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
    def __init__(self, program_name, menu_name, previous_page, root_page, exiting_message, properties):
        super().__init__(program_name=program_name, menu_name=menu_name,
                         previous_page=previous_page, root_page=root_page,
                         exiting_message=exiting_message)
        self.properties = properties

    #add_new ne veut rien dire renommer en submit ou run  par exemple
    def add_new(self, properties) -> dict:   # essayer de rendre add_new_tournament et add_new_player générique !! cf ask_properties() dans class GenericInputs()
        print(self.program_name, '\n', self.menu_name, '\n')
        # Où est ce que je recupère la liste des properties et comment je fais le tri par rapport à l'objet, à continuer elaboration/redaction!
        # reflechir par rapport à add tournament et add player
        # properties = ['last_name', 'first_name', 'birthdate', 'gender', 'ranking']
        # ou
        # properties = ['name', 'location', 'start_date', 'end_date',
        #             'players_identifier', 'time_control', 'description', 'rounds_list', 'rounds']
        # cette partie est valable, mais ask_property pas codée
        properties_dict = {}
        for _property in properties:
            properties_dict[_property] = GenericInputs().ask_property()
        print(properties)
        return properties_dict
