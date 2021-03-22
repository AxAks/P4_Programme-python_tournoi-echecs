# coding=utf-8

"""
Generic Class for Forms
"""
from views.menus.menu import Menu


class Form(Menu):
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """
    def __init__(self, program_name, menu_name):
        super().__init__(program_name=program_name, menu_name=menu_name,
                         previous_page=None, root_page=False,
                         exiting_message='Leaving Form')

    def add_new(self, ):   #essayer de rendre add_new_tournament et add_new_player générique !!
        print(self.program_name, '\n', self.menu_name, '\n')
        # Où est ce que je recupère la liste des properties et comment je fais le tri par rapport à l'objet, dans les classes filles... à continuer elaboratino redaction!
        properties = {}
        properties_dict = {}
        for _property in properties:
            properties_dict[_property] = ask_property()
